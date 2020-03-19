import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")

cur = conn.cursor()
try:
    sql2 = "SELECT * FROM `account` WHERE `acc`='accC'"
    sql = "SELECT * FROM account WHERE acc = %s"
    cur.execute(sql2)
    rs = cur.fetchall()
    print(rs)
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
