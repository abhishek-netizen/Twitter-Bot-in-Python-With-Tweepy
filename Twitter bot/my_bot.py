# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:01:04 2021

@author: Abhish
"""
import tweepy
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
KEY = ''
SECRET = '' 



auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(KEY,SECRET)

api = tweepy.API(auth)
api


FILE_NAME = 'last_seen.txt'

#Reading
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
#Writing
def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return




#duplicate_text = "twitter bot reporting live !!!"
#
#try:
#    api.update_status(duplicate_text)
#except tweepy.TweepError as error:
#    if error.api_code == 187:
#        print(duplicate_text)
#    else:
#        raise error
        
tweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode="extended")
#print(tweets[0].text)

def replay():
    for tweet in reversed(tweets):
        if '#100DaysOfCode' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status('@' + tweet.user.screen_name + ' Keep-up the good work', tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)
while True:
    replay()
    time.sleep(15)