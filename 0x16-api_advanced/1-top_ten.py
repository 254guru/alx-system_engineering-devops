#!/user/bin/python3
"""
import module
"""
import requests


def top_ten(subreddit):
    """
    function that queries the reddit API and prints tittles of
    first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            print(post['data']['title'])
    elif response.status_code == 404:
        print(None)
    else:
        print(f"Error: {response.status_code}")
        print(None)
