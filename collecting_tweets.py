import json
import time
import os
import sys
import tweepy as tw
import pandas as pd

# Twitter API keys
consumer_key = 'Your Consumer key'
consumer_secret = 'Your Consumer secret'
access_token = 'access token'
access_token_secret = 'access token secret'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify= True)


search_words = "canada Covid19"  #Key words


#saving_tweets
filename = 'January'
columns = ["tweet_id","tweet_text","verified","followers_count","friends_count","user_created_at","retweet_count"]

Raw_tweets = pd.DataFrame(columns=columns)

until_date = "2020-02-01"##year-month-day

from_date = "2020-01-01"
# Collecting tweets
tweets = tw.Cursor(api.search, q=search_words, lang="en",tweet_mode="extended",fromDate = from_date, toDate = until_date).items()


for tweet in tweets:
    try:
        current_tweet = tweet.extended_entities
    except:
        current_tweet = "NaN"

    tweet_id = tweet.id
    verified = tweet.user.verified
    followe_count = tweet.user.followers_count
    friends_count = tweet.user.friends_count
    account_created_time = tweet.created_at
    retweet_counts = tweet.retweet_count
    try:
        if tweet.retweeted_status is None:
            o = 'False'
            tweet_text = tweet.full_text

        else:
            o = 'True'
            tweet_text = tweet.retweeted_status.full_text

    except:
        o = 'False'
        tweet_text = tweet.full_text

    Raw_tweets = Raw_tweets.append({"tweet_id": tweet_id , "tweet_text": tweet_text,
                                        "verified": verified,"followers_count":followe_count,
                                        "friends_count":friends_count,"user_created_at":account_created_time,
                                        "retweet_count": retweet_counts}, ignore_index=True)

Raw_tweets = Raw_tweets.drop_duplicates(subset=['tweet_id'])
Raw_tweets.to_csv("Raw"+filename+".csv")


