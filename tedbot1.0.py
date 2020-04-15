#!/usr/bin/env python
import sys
from twython import Twython

apiKey = '...'
apiSecret = '...'
accessToken = '...'
accessTokenSecret = '...'

import random
# Create random number to correspond with paragraph number
for x in range(1):
    T=random.randint(1,230)
print(T)
num = str(T)

import re
teddy = open("tedm.txt", "r")
searchnum = num
for line in teddy.readlines():
    if searchnum in line:
        positionofa = line.index(searchnum)
#        print('"',line[positionofa+4:positionofa+270],'..."-Ted')
        A=line[positionofa+4:positionofa+269]+"... #Ted"

with open("tedtalks.txt", "w") as txt_file:
    for durr in A:
        txt_file.write("".join(durr))

Tweet = open("tedtalks.txt", "r")

finaltweet = Tweet.read()
tweetStr = finaltweet

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)

print("Tweeted: " + tweetStr)
