import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")

cur = conn.cursor()
try:
    sql2 = "SELECT * FROM `account` WHERE `acc`='accC'"
    sql = "SELECT * FROM account WHERE acc = %s"
    # sql = "SELECT * FROM customers WHERE address = %s"
    adr = tuple()  # ("accB", )
    strA = input("Input acc: ")
    # mycursor.execute(sql, adr)
    adr += (strA,)
    cur.execute(sql, adr)
    rs = cur.fetchall()
    if not rs:
        print("Acc do not exits!\n")
    else:
        print(rs)
        print("TEST")
    print("===================")
    for row in rs:
        if row[1] == "accE":
            print("=== Account info ===")
            print(row)
            break
        else:
            print("Do not exits!\n")
    print("OK")
except:
    conn.rollback()
conn.close()
