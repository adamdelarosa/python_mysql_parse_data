import MySQLdb, csv, sys

conn = MySQLdb.connect("localhost","root","root","PRO_STORE" )
c = conn.cursor()
csv_data=csv.reader(file("var/log/store.log"))
for row in csv_data:
    c.execute("INSERT INTO STORE_DATA SET DATE_TIME = %s", row)
    print row

conn.commit()
c.close()