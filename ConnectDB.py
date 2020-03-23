import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")

cur = conn.cursor()
try:
    sqlSelect = "SELECT * FROM account WHERE acc = %s"
    # adr = tuple()  # ("accB", )
    strA = input("Input acc: ")
    acc = (strA,)
    # mycursor.execute(sql, adr)
    # adr += (strA,)
    cur.execute(sqlSelect, acc)
    rs = cur.fetchall()
    if not rs:
        print("Acc do not exits!\n")
    else:
        print("=== Account info ===")
        print("ID\tAccount\tBalance")
        for row in rs:
            print("%s\t%s\t%d" % (row[0], row[1], row[2]))
        print("====================")
    print("OK")
except:
    conn.rollback()
conn.close()
