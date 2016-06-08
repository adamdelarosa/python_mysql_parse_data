import MySQLdb, csv, sys

conn = MySQLdb.connect("localhost","root","root","PRO_STORE" )
c = conn.cursor()
csv_data=file.read(file("var/log/store.log"))

with open("var/log/store.log", "r") as sports:
    lines = sports.readlines()

for line in lines:
    data = line.split()

    date_time = data[0]
    product = data[1]
    kind = data[2]
    value = data[3]

    #data = csv_data.split()
    #number = data[0]
    #value = data[1]
    #c.execute("INSERT INTO STORE_DATA SET DATE_TIME = %s", row)
    #print row
    print date_time
    print product
    print kind
    print value

conn.commit()
c.close()