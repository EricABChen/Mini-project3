import mysql.connector
import twitter


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
mycursor = mydb.cursor()


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
