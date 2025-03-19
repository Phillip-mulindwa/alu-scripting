#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """
    A function that fetches and prints the titles
    of the top ten hot posts from a subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        params={"after": None},
        allow_redirects=False,
        headers=headers,
    )

    if response.status_code != 200:
        print(None)
        return

    json_data = response.json()
    data = json_data.get("data", {}).get("children", [])
    if not data:
        print(None)
        return

    # Print the titles of the first 10 posts
    for post in data[:10]:
        print(post.get("data", {}).get("title", None))
