from flask import Flask,request
# import flask module

import mysql.connector
# To connect make connection with database

app = Flask(__name__)
#Constructor with argument

@app.route('/login',methods = ['POST'])
#Route() function in which we can  represent URL ,
#also, define methods  that used to send data to a server to create/update a resource
def login():
   if request.method == 'POST':# request method to use 'POST'
      username = request.form['username']# syntax to use get() method &&&&
      password = request.form['password']
      gender = request.form['Gender']
      email = request.form['email']
      phonecode = request.form['phonecode']
      phonecode=str(phonecode)
      phone = request.form['phone']
      phone=str(phone)

      db = mysql.connector.connect(host="localhost", user="root", password="Server@123", database="12feb")
      print("connection successful")
      cursor = db.cursor()

      sql = "INSERT INTO inser(username, password, gender,email, phonecode,phone) VALUES (%s, %s, %s, %s, %s,%s)"

      val = ([username, password, gender, email, phonecode, phone])
      cursor.execute(sql, val)
      db.commit()
      db.close()
      return "thank you, your database is saved"


if __name__ == '__main__':
   app.run(debug = True)

