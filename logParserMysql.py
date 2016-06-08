#!/usr/bin/python

import MySQLdb

print 'Data parser . . . '

# Open database connection
db = MySQLdb.connect("localhost","root","root","STORE_DATA" )

cursor = db.cursor()

file = open('var/log/store.log', 'r')

file_content = file.read()
print file_content
file.close()

query = "INSERT INTO STORE_DATA VALUES (%s)"

cursor.execute(query, (file_content,))

print file_content

db.commit()
db.close()