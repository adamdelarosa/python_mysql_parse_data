import MySQLdb, csv, sys

conn = MySQLdb.connect("localhost","root","root","PRO_STORE" )
c = conn.cursor()
csv_data=csv.reader(file("var/log/store.log"))
for row in csv_data:
    c.execute("UPDATE STORE_DATA SET DATE_TIME = %s", row)
    print row
    #c.execute("INSERT INTO STORE_DATA (DATE_TIME, PRODUCT) VALUES ('%s', '%s')" % tuple(row))

conn.commit()
c.close()