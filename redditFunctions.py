import requests
import json
import pandas as pd
import authFile as authFile
import config as cfg

#Reddit API info:
#https://www.reddit.com/prefs/apps
#https://www.reddit.com/wiki/api#wiki_reddit_api_access
#https://github.com/reddit-archive/reddit/wiki/API


reddit_API = authFile.oauth_login()
TOKEN = reddit_API.json()['access_token']
headers = {**cfg.headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

def get_hot_posts():
    res = requests.get("https://oauth.reddit.com/r/apexlegends/hot", headers=headers)

    #pandas documentation
    #https://pandas.pydata.org/docs/reference/frame.html
    df = pd.DataFrame()  # initialize dataframe

    # loop through each post retrieved from GET request
    for post in res.json()['data']['children']:
        # append relevant data to dataframe
        df = df.append({
            #'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            #'selftext': post['data']['selftext'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score']
        }, ignore_index=True)

    posts = df.to_markdown(tablefmt="grid")
    #formatted = json.dumps(postsDict, indent=2)
    print(posts)

def get_new_posts():
    res = requests.get("https://oauth.reddit.com/r/apexlegends/new", headers=headers)

    #pandas documentation
    #https://pandas.pydata.org/docs/reference/frame.html
    df = pd.DataFrame()  # initialize dataframe

    # loop through each post retrieved from GET request
    for post in res.json()['data']['children']:
        # append relevant data to dataframe
        df = df.append({
            #'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            #'selftext': post['data']['selftext'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score']
        }, ignore_index=True)

    posts = df.to_markdown(tablefmt="grid")
    #formatted = json.dumps(postsDict, indent=2)
    print(posts)