#!/usr/bin/python3
"""
import modules
"""
import sys
import requests
from collections import Counter


def count_words(subreddit, word_list):
    # Reddit API endpoint for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # Set a custom User-Agent to avoid issues with Reddit API
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the titles of the current page
        data = response.json()
        posts = data['data']['children']

        # Initialize counts dictionary
        counts = Counter()

        # Update counts with occurrences of words in the titles
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word_lower = word.lower()
                # Check for word boundary to avoid partial matches
                if f" {word_lower} " in f" {title} ":
                    counts[word_lower] += 1

        # Recursive call with the 'after' parameter for the next page
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list)
        else:
            # No more pages, print the counts in descending order
            print_counts(counts)
    elif response.status_code == 404:
        # Subreddit not found, print nothing
        pass
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")


def print_counts(counts):
    # Sort counts in descending order by count, then alphabetically by word
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted counts
    for word, count in sorted_counts:
        print(f"{word}: {count}")
