import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import psycopg2 as pgsql
import random

get_users_books_query = """
                        select b.title
                        from books as b
                        join users_books as ub
                            on b.book_id = ub.book_id
                        where ub.user_id = %s;
                        """

books_genres_columns = ['title', 'rating', 'genres']

cosine_sim_file_path = 'rec_files/cosine_similarity.csv'


class RecommendationEngine:

    def __init__(self):
        self.db_connection = None
        self.db_cursor = None
        self.books_genres_df = None

    def connect_to_db(self, db_name, user, password, host) -> None:
        try:
            self.db_connection = pgsql.connect(dbname=db_name, user=user,
                                               password=password, host=host)
            self.db_cursor = self.db_connection.cursor()
        except pgsql.DatabaseError as e:
            print(f'Error {e}')
            self.db_cursor.close()
            self.db_connection.close()

    def close_db_connection(self) -> None:
        self.db_cursor.close()

    def get_titles_by_uid(self, user_id) -> list:
        self.db_cursor.execute('''select b.title
                        from books as b
                        join users_books as ub
                            on b.book_id = ub.book_id
                        where ub.user_id = %s;
                        ''', str(user_id))
        user_books_list = list(self.db_cursor.fetchall())
        return [title_tuple[0] for title_tuple in user_books_list]

    def get_active_users_ids(self) -> list:
        self.db_cursor.execute('''select user_id
                             from users_books
                             group by user_id;
                             ''')
        users_list = list(self.db_cursor.fetchall())
        return [user_tuple[0] for user_tuple in users_list]

    def get_indexes_in_cos_sim_matrix(self, titles_list) -> list:
        if self.books_genres_df.empty:
            return []
        titles_list = self.books_genres_df.loc[self.books_genres_df.title.isin(titles_list)]
        return [i for i in titles_list.index]

    def get_titles_in_cos_sim_matrix(self, indexes_list) -> list:
        if self.books_genres_df.empty:
            return []
        return self.books_genres_df.iloc[indexes_list].title.to_list()

    def process_genre_based_filtering(self) -> None:
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0)
        tfidf_matrix = tf.fit_transform(self.books_genres_df['genres'])

        with open(cosine_sim_file_path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            i = 0
            while i < tfidf_matrix.shape[0]:
                cosine_sim = linear_kernel(tfidf_matrix[i:i + 1000], tfidf_matrix)
                print(f'Updating cosine similarity matrix: {i + 1000} completed')
                writer.writerows(cosine_sim)
                i += 20000
                del cosine_sim

    def load_data(self) -> None:
        self.db_cursor.execute('''select b.title, avg(b.rating), string_agg(g.genre_description, ', ')
                     from books as b
                     join books_genres as bg ON b.book_id = bg.book_id
                     join genres g on g.genre_id = bg.genre_id
                     group by b.title;''')
        self.books_genres_df = pd.DataFrame(self.db_cursor.fetchall(), columns=books_genres_columns)

        self.process_genre_based_filtering()

    def get_recommendation(self, title_idx) -> list:
        column = pd.read_csv('cosine_similarity.csv', usecols=[title_idx], header=None).to_numpy()
        idx = 0
        sim_scores = list(enumerate(column))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]
        books_indices = [i[0] for i in sim_scores]
        return books_indices

    def filter_recommendations(self, user_id, titles_recommended) -> list:
        # 5. filter data
        # still have no filtering
        # just randomly gets titles to recommend
        indices = random.sample(range(len(titles_recommended)), 7)
        result = []
        for index in indices:
            result.append(titles_recommended[index])
        return result

    def refresh_users_recommendations_table(self) -> None:
        self.load_data()
        user_ids_list = self.get_active_users_ids()
        for each_user in user_ids_list:
            recommendations_list_idx = []
            titles_list = self.get_titles_by_uid(each_user)
            titles_index_list = self.get_indexes_in_cos_sim_matrix(titles_list)
            for each_title in titles_index_list:
                recommendations_list_idx += self.get_recommendation(each_title)
            titles_recommended = self.get_titles_in_cos_sim_matrix(recommendations_list_idx)
            # debug purposes
            print(f'user {each_user}')
            print(self.filter_recommendations(each_user, titles_recommended))

    def get_recommendations(self, user_id, genre_list=None, mode=0):
        """
        recommendations will be populated from database's users_recommendations table
        if there is no recommendation for a specific user_id
        we will just search for a same genre books in database's books table
        """
        pass


def main():
    # so we now need to update the whole table of user recommendations
    rec_engine = RecommendationEngine()
    rec_engine.connect_to_db('book_finder', 'postgres', 'password', 'localhost')
    rec_engine.refresh_users_recommendations_table()
    rec_engine.close_db_connection()


if __name__ == '__main__':    
    main()
