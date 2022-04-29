""" 
Modul pro answer_machine na vyhledavani informaci on-line
"""

import argparse
import requests

from gooey import Gooey

ANSWER_ENDPOINT = "https://api.duckduckgo.com"
parameters = {
    "format": "json",
    "q": "",
}

@Gooey
def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description = "Will find answers online")
    parser.add_argument("query", help="Tell me what you want to know")
    args = parser.parse_args()

    query = args.query
    parameters["q"] = query

    returned = requests.get(ANSWER_ENDPOINT, parameters)
    obj = returned.json()
    print(obj["Abstract"])


if __name__== "__main__":
    main()
