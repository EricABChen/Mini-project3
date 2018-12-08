import tweepy
import mysql.connector
import twitter
from google.cloud import vision
import pymysql
import sys

# Set API
# use your own token to authorize the function of the API
consumer_key = "your API key"
consumer_secret = "your API secret key"
access_key = "your access token"
access_secret = "your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


my_client = vision.ImageAnnotatorClient()

# Connect to database
my_db = pymysql.connect(<SERVER>, <USERNAME>, <PASSWORD>, <DATABASE_NAME>)
try:
    print("Connecting...")
    cursor = db.cursor()
    print("Connected!")
except:
    print("Fail to connect to the database, please check your environment.")

# Set the number of users
num_of_users = 10

# Set the number of images
num_of_image = 100

# Get users
counter = api.friends(count = num_of_users)

# Get entries of each user
try:
  for i in range(0, len(counter)):
      tweets = api.user_timeline(counter[i].id, count = num_of_image)
      for j in range(0, len(tweets)):
          tweet = tweets[j]
          get_URL = tweets[j].entities.get("get_URL")
          if get_URL is not None:
              img_url = str(get_URL[0].get("get_URL_url_https"))
except:
  pass
cursor.execute(new_sql)
db.commit()
print("Seccessfully created.")

# Close connection
db.close()


def filter():
  '''search and find'''
    Open = open(sys.argv[1], 'r')
    
    # try to connect to the database
    try:
        my_db = pymysql.connect()
        cursor = my_db.cursor()
        print("Success.")
    except:
        print("Failed.")

    cursor.execute(sql)
    results = cursor.fetchall()
    
    for item in results:
        user = item[0]
        followers = item[1]
        print('user', user, 'have followers includes:', followers)
   
    # Close connection
    db.close()

def insert(sql, val):
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      passwd="yourpassword",
      database="mydatabase"
    )
    mycursor = mydb.cursor()    
    mycursor.execute(sql, val)    
    mydb.commit() 
    print(mycursor.rowcount, "record inserted.")
    
def search():
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      passwd="yourpassword",
      database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute()
    myresult = mycursor.fetchall()       

    for user in myresult:
      print(x)
      

def delete(sql,adr):
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      passwd="yourpassword",
      database="mydatabase")

    mycursor = mydb.cursor()
    mycursor.execute(sql, adr)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
