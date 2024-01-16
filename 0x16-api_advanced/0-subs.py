#!/usr/bin/python3
"""
import module
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the reddit API and returns the
    number of subscribers
    """
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = request.get(url, headers=headers)
        response.raise_for_status() # raises stored HTTPError, if one occured
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        return 0
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return 0
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return 0
    except requests.exceptions.RequestException as err:
        print ("Something went wrong", err)
        return 0

    json_data =response.json()
    if 'data' in json_data and 'subscribers' in json_data['data']:
        return int(json_data['data']['subscribers'])
    else:
        return 0
