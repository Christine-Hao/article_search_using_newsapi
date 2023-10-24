import json
from argparse import ArgumentParser
from pathlib import Path
from newscover.newsapi import fetch_latest_news

api_key = "8fea865a1a4448d1adcd64e21d1b43ae"


def get_file_path():
    file_path = Path(__name__).parent
    return file_path


def main():
    '''
    CLI tool sitting in the newscover.collector that has the following behavior
        Python -m newscover.collector -k <api_key> [-b <# days to lookback>] -i <input_file> -o <output_dir>
    '''

    file_path = get_file_path()

    parser = ArgumentParser()

    parser.add_argument("-k", "--api_key", required=True,
                        help="api_key for the api call")
    parser.add_argument("-b", "--lookback_days", required=False,
                        help="# days to look back from the inital day")
    parser.add_argument("-i", "--input", required=True,
                        help="the name of the input file")
    parser.add_argument("-o", "--output", required=True,
                        help="the name of the output file")

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        keywords = json.load(f)

    lookback_days = int(args.lookback_days)
    articles = {}
    for key in keywords.keys():
        search_results = fetch_latest_news(
            args.api_key, keywords[key], lookback_days)
        articles[key] = search_results

    # write it to the output file
    with open(args.output, 'w') as o:
        json.dump(articles, o)


if __name__ == "__main__":
    main()
