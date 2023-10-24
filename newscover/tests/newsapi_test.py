import unittest
from newscover.newsapi import fetch_latest_news
from datetime import datetime, timedelta


class GeneralCheckTests(unittest.TestCase):
    def fail_when_no_keyword(self):
        '''ensure that fetch_latest_news fails when no news_keywords are provided.'''
        with self.assertRaises(ValueError):
            fetch_latest_news("8fea865a1a4448d1adcd64e21d1b43ae", [])

    def timeFrame_check(self):
        '''
        ensure that when lookback_days is set, it doesn’t produce articles outside that timeframe
        '''
        articles = fetch_latest_news(
            "8fea865a1a4448d1adcd64e21d1b43ae", ["Apple"], 10)
        last_possible_time = datetime.now().date() - timedelta(10)

        all_within_date = True
        for article in articles:
            # Convert it to a datetime object
            published_date = datetime.strptime(
                article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            if published_date > last_possible_time:
                all_within_date = False
                break

        self.assertTrue(all_within_date,
                        "Some articles are outside of the expected timeframe")

    def contains_non_alphabetic(self):
        '''
        ensure that fetch_latest_news fails when a keyword contains a non-alphabetic character.
        '''
        with self.assertRaises(ValueError):
            fetch_latest_news("8fea865a1a4448d1adcd64e21d1b43ae", [
                              "-vf", "London", "2yes"], 10)


if __name__ == "__main__":
    unittest.main()
