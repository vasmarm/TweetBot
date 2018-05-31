
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
import datetime
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[2]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[3]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
counter = 0


# In[4]:


# Create a function that tweets
# Setup Tweepy API Authentication
def TweetCall():
    api.update_status("Tweet at " + str(datetime.datetime.now()) + " number " + str(counter+1))
    # Print success message
    print("Tweet Done")


# In[5]:


# Create a function that calls the TweetOut function every minute
def TweetOut():
    TweetCall()
    time.sleep(60)


# In[ ]:


# Infinite loop
while True:
    TweetOut()

