from recommendation_engine import RecommendationEngine


def main():
    # so we now need to update the whole table of user recommendations
    rec_engine = RecommendationEngine()
    rec_engine.connect_to_db('book_finder', 'postgres', 'nika23v05super01', 'localhost')
    rec_engine.run_recommendations_update()
    rec_engine.close_db_connection()


if __name__ == '__main__':
    main()
