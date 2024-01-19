#!/usr/bin/python3
"""
import module
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Reddit API endpoint for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # Set a custom User-Agent to avoid issues with Reddit API
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Add 'after' parameter if it exists
    if after:
        url += f"&after={after}"

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the posts
        data = response.json()
        posts = data['data']['children']

        # Add titles of the current page to the hot_list
        hot_list.extend([post['data']['title'] for post in posts])

        # Check for the presence of the 'after' parameter in the response
        after = data['data']['after']
        if after:
            # Recursive call with the 'after' parameter for the next page
            return recurse(subreddit, hot_list, after)
        else:
            # No more pages, return the final hot_list
            return hot_list
    elif response.status_code == 404:
        # Subreddit not found, return None
        return None
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return None
