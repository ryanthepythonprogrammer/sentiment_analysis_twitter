from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
import datetime
import time
import sentiment_mod as s
import os
import sys
from grapher import graphing as g

ckey=""#enter your own twitter api ckey, csecret, atoken, and asecret here
csecret=""
atoken=""
asecret=""

authorization = OAuthHandler(ckey, csecret)
authorization.set_access_token(atoken, asecret)

api = tweepy.API(authorization)

print("Loaded API...")

users = "ryanp2601"
passkeys = "Ryan1601"

if os.path.exists("twitter_out.txt") == True:
    os.remove("twitter_out.txt")

else:
    open("twitter_out.txt", "w+")

lol = False

while not lol == True:

    user = input("Please input your username: ")
    passkey = input("Please input your passkey: ")

    while user == users and passkey == passkeys:

        if os.path.exists("twitter_out.txt") == True:
            os.remove("twitter_out.txt")

        else:
            open("twitter_out.txt", "w+")

        username = input("Please enter the username of the patient: ")

        docname = "twitter_out.txt"

        num = int(input("Please enter the number of days you would like to run the engine on: "))

        variable1 = 0

        def data(var, num, doc, username, get_api):

            page = 1
            deadend = False

            while True:
                tweets = get_api.user_timeline(username, page = page)

                for tweet in tweets:
                    tweet_encoded = str(tweet.text.encode("utf-8"))

                    print("Loading Tweets")

                    if (datetime.datetime.now()-tweet.created_at).days < num:

                        sentiment_value, confidence = s.sentiment(tweet_encoded)

                        if confidence*100 >= 80:
                            output = open(doc,"a")
                            output.write(sentiment_value)
                            output.write("\n")
                            output.close()
                            print("Adding Sentiment to Document")

                        else:
                            output = open(doc,"a")

                        print((datetime.datetime.now()-tweet.created_at).days)

                    else:
                        deadend = True
                        return

                if not deadend:
                    page+=1                    
        data(variable1, num, docname, username, api)
        g()
        break

    var2 = input("Would you like to exit the program? (Yes/No) ")

    if var2 == "no":
        print("Continuing...")

    elif var2 == "No":
        print("Continuing...")

    elif var2 == "Yes":
        exit()

    elif var2 == "yes":
        exit()

    else:
        print("""Incorrect Reply.
        Please Try again""")


