#!/usr/bin/python3
"""
Function that uses the Reddit API and returns the
number of subscribers for a given subreddit on Reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Takes a subreddit name, and returns the number of subscribers
    new line
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]

    return 0
