#!/usr/bin/python

import MySQLdb

print 'Creating new tables . . . '

# db connection
db = MySQLdb.connect("localhost","root","root","PRO_STORE" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS STORE_DATA")

# SQL syntax
sql = """CREATE TABLE STORE_DATA (
         DATE_TIME  CHAR(20) NOT NULL,
         PRODUCT  CHAR(20),
         KIND CHAR(20),
         VALUE CHAR(1))"""

cursor.execute(sql)
# Close connection
db.close()