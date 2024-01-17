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
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    user_agent = {'User-Agent': 'Python/requests'}

    payload = {'limit': '10'}

    res = requests.get(api_uri, headers=user_agent,
                       params=payload, allow_redirects=False)

    if res.status_code in [302, 404]:
        print('None')
    else:
        res_json = res.json()

        if res_json.get('data') and res_json.get('data').get('children'):
            hot_posts = res_json.get('data').get('children')

            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
