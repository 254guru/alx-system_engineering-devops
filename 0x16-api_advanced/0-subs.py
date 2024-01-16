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

    response = request.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else response.status_code == 404:
        return 0
