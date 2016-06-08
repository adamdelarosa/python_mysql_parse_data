import MySQLdb

conn = MySQLdb.connect("localhost","root","root","PRO_STORE" )
c = conn.cursor()

with open("var/log/store.log", "r") as store_value:
    lines = store_value.readlines()

for line in lines:
    data = line.split()

    #Data collect
    date_time = data[0]
    product = data[1]
    kind = data[2]
    value = data[3]

    #c.execute("INSERT INTO STORE_DATA SET DATE_TIME = %s", row)
    #Print data store:
    print "DATE_TIME: " + date_time + " PRODUCT: " + product + " KIND: " + kind + " VALUE: " + value

conn.commit()
c.close()