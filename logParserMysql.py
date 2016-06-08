import MySQLdb

conn = MySQLdb.connect("localhost","root","root","PRO_STORE" )
c = conn.cursor()

with open("var/log/store.log", "r") as store_value:
    lines = store_value.readlines()
print "Data moving to mysql . . ."

for line in lines:
    data = line.split()

    #Data collect:
    data_date_time = data[0]
    data_product = data[1]
    data_kind = data[2]
    data_value = data[3]

    #SQL:
    c.execute("""INSERT INTO STORE_DATA (date_time, product, kind, value)
        VALUES(%s, %s, %s, %s)""", (data_date_time, data_product, data_kind,data_value))

    print "DATE_TIME: " + data_date_time + " PRODUCT: " + data_product + " KIND: " + data_kind + " VALUE: " + data_value

conn.commit()
print "Closing connection . . ."
c.close()

print "done."