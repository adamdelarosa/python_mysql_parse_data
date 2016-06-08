#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","store_data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         DATE_TIME  CHAR(20) NOT NULL,
         PRODUCT  CHAR(20),
         KIND CHAR(20),
         VALUE CHAR(1))"""

cursor.execute(sql)

# disconnect from server
db.close()