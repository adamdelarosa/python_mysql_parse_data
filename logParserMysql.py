#!/usr/bin/python

import MySQLdb

print 'Data parser . . . '

# Open database connection
db = MySQLdb.connect("localhost","root","root","PRO_STORE" )

cursor = db.cursor()

file = open('var/log/store.log','r')

file_content = file.read()
print file_content
file.close()

#query = "INSERT INTO STORE_DATA (DATE_TIME, PRODUCT, KIND, VALUE) VALUES ('%s','W','d','W')"
for row in file_content:
    print row
    query = ("""INSERT INTO STORE_DATA (DATE_TIME, PRODUCT, KIND, VALUE) VALUES (%s,%s,%s,%s),raw""")

cursor.execute(query)

db.commit()
db.close()