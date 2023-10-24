import requests
from datetime import datetime, timedelta


def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    # Input Validation
    # None or empty
    if not news_keywords or news_keywords == []:
        raise ValueError("There must be at least one keyword")
    for keyword in news_keywords:
        if not keyword.isalnum():
            raise ValueError(
                "One of the keyword contains non-alphannumric values")

    ENDPOINT = "https://newsapi.org/v2/everything"
    LANGUAGE = "en"
    end_date = datetime.now().date()
    # A timedelta object represents a duration,
    # the difference between two dates or times.
    start_date = end_date - timedelta(days=lookback_days)

    for keyword in news_keywords:
        params = {
            "q": keyword,
            "language": LANGUAGE,
            "apiKey": api_key,
            "from": start_date.isoformat(),
            "to": end_date.isoformat(),
        }
    # For the date
    response = requests.get(ENDPOINT, params)
    data = response.json()

    list_of_articles = data['articles']

    return list_of_articles


def main():
    fetch_latest_news("8fea865a1a4448d1adcd64e21d1b43ae", [
                      "Apple"], 10)


if __name__ == "__main__":
    main()
