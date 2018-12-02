# -*- coding: utf-8 -*-

import tweepy
from google.cloud import vision
import pymongo


# use your own token to authorize the function of the API
consumer_key = "your API key"
consumer_secret = "your API secret key"
access_key = "your access token"
access_secret = "your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

vision_client = vision.ImageAnnotatorClient()

# Connect to mongoDB 
# Important note: replace the <PASSWORD> with your own to get access to the database
my_client = pymongo.MongoClient("mongodb+srv://Aprilius:<PASSWORD>@cluster0-2rq5o.mongodb.net/test?retryWrites=true")
my_db = my_client["miniProject_3"]
try:
    db = my_client.twitter
    print("Successfully Connected to the MongoDB")
except:
    print("Fail to connect to the MongoDB, please check your token and your environment.")
    

def search():
    user = []
    label = []
    date = []
    index = []
    display = []
    
    for i in my_client.downloads.find({'label': label}):
    	user.append(i['user_name'])
    	date.append(i['date'])
    	index.append(i['index'])
    	display.append(i['display'])
    
    if len(index) == 0:
        print("The data you are looking for do not exist!")
    else:
        for i in range(0,len(index)):
            print("Starts searching")
            print("No.",i+1," label",label)
            print("user:",user[i])
            print("date:",date[i])
            print("index:", index[i])   
            print("searched:",display[i])
            
            
def delete(myquery):
    x = my_db.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")      


def display():
    print("Currently there are ",my_db.count(),"users in the database")
    average = 0
    dic = []
    for user in my_db.find():
        print("The user:",user)
        average = average + user.get('img_num')
        dic2 = user.get('description').split(',')
        for j in dic2:
            dic.append(j)
    if (my_db.count() > 0):
        print("Some statistics:")
        print("The most popular description is",(max(dic.keys())))
    return


def insert(mylist = []):
    x = my_db.insert_many(mylist)
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)


def update(myquery, newvalues):
    my_db.update_one(myquery, newvalues)
    #print the result after the update:
    for x in my_db.find():
      print(x)
      



# check the database is successfully created
dblist = my_client.list_database_names()
if "miniProject_3" not in dblist:
    print("Fail to create a new MongoDB, please check your environment setting.")
exit()
