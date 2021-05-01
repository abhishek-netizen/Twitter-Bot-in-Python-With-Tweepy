# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:16:53 2021

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




               

#hashtag = "#Bengaluru OR #Verified OR #Ambulance OR #bangalorecovid OR #OxygenCrisis OR #OxygenShortage OR #bangalorecovidhelp OR #oxygen OR #bed OR #karnatakacovid OR #covidemergency OR #covid19indiahelp OR #icubeds #ventilatorbeds OR #wearebengaluru OR #peakbengaluru OR #covid19 OR covidhelp OR #coronavirus OR #covid OR #corona OR #stayhome OR #quarantine OR #lockdown OR #staysafe OR #socialdistancing OR #pandemic OR #stayathome"

hashtag = {
"hashtags":["#Bengaluru","#Verified","#Ambulance","#bangalorecovid","#OxygenCrisis","#OxygenShortage","#bangalorecovidhelp","#oxygen","#bed","#karnatakacovid","#covidemergency","#covid19indiahelp","#icubeds","#ventilatorbeds","#wearebengaluru","#peakbengaluru","covidhelp","#sosbengaluru"]
}

tweetnumber = 10

for i in range(17):
    for hash in hashtag.values():
        tweets = tweepy.Cursor(api.search, hash[i]).items(tweetnumber)
        

#tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(3)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(5)
searchBot()


