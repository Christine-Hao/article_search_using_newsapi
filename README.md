---------------------Overview---------------------

---------------------Running---------------------

To run the script, fo to the root folder and run :
-> "python -m newscover.tests.newsapi_test" for unit tests

-> "python -m newscover.collector.main" to run a script

-> To know how to use positional argument, do
"python -m newscover.collector.main --help" and you get:
usage: main.py [-h] -k API_KEY [-b LOOKBACK_DAYS] -i INPUT -o OUTPUT

    options:
    -h, --help            show this help message and exit
    -k API_KEY, --api_key API_KEY
                            api_key for the api call
    -b LOOKBACK_DAYS, --lookback_days LOOKBACK_DAYS
                            # days to look back from the inital day
    -i INPUT, --input INPUT
                            the name of the input file
    -o OUTPUT, --output OUTPUT
                            the name of the output file

Some additional knowledge

------------Unit tests-----------------
The expression if not news_keywords: checks for "falsy" values of the variable news_keywords. In Python, some values are considered to be "truthy" (evaluating to True in a boolean context) and others are "falsy" (evaluating to False in a boolean context).

For the expression if not news_keywords:, if news_keywords holds a "falsy" value, the code inside the if block will execute.

Here are some "falsy" values in Python:

An empty string ("")
An empty list ([])
An empty tuple (())
An empty dictionary ({})
The number zero (both 0 and 0.0)
None
False
