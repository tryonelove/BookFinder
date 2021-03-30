from recommendation_engine import RecommendationEngine
import sys
import argparse


def main(args):
    db_name = args.database
    username = args.username
    password = args.password
    host = args.host

    # so we now need to update the whole table of user recommendations
    rec_engine = RecommendationEngine()
    if rec_engine.connect_to_db(db_name, username, password, host):
        print(f'Error connecting to the database {db_name}')
    rec_engine.run_recommendations_update()
    rec_engine.close_db_connection()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-hst', '--host')
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    parser.add_argument('-db', '--database')
    args = parser.parse_args()
    main(args)