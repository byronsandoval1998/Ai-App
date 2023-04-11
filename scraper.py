import praw
import pandas as pd
import os

reddit = praw.Reddit(client_id=os.environ.get('C_ID'),         
                               client_secret=os.environ.get('R_SECRET'),     
                               user_agent="Lit Scraper",
                               username=os.environ.get('UNAME'),
                               password=os.environ.get('UPASS'), )        

subred = reddit.subreddit("POESIA")

hot = subred.hot(limit = 11)

for i in hot:
    print(i.title)
    print(i.selftext)