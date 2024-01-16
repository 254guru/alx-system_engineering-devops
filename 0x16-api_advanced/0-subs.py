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

    response = request.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    elif response.status_code == 404:
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0


if __name__ == '__main__':
    subreddit_name = input("Enter the subreddit name: ")
    result = number_of_subscribers(subreddit_name)
    print(f"Number of subscribers: {result}")
