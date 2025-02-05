

import argparse
import json
import sys
import urllib
import urllib.request

import duckdb


def main(url):
    print(f"{url=}")

def querysomething(url):
    conn = duckdb.connect(config = {"allow_unsigned_extensions": "true"})
    return conn.sql(f"SELECT * FROM '{url}';")
    #return conn.sql(f'SELECT * FROM read_json_auto("{url}")')


def getjson(url):
    """Retreuves URL from the location.
    
    Returns: string version of the result.
    """
    page = fetchdata(url, isjson=False)
    return page


def runquery(database, query):
    """Runs a query on the db given a query.

    Returns: string - result set
    """
    return None


def fetchdata(url, isjson=True):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/',
        'DNT': '1',  # Do Not Track request header
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }


    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        if isjson:
            return json.loads(data)
        else:
            return data




if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--url", type=str, help="some URL")
    parser.add_argument("--output", type=str, default="output.txt", help="Save the output here")

    args = parser.parse_args()

    if args.url:
        main(url=args.url)
    else:
        parser.print_help(sys.stderr)
