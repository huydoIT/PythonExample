import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")
cur = conn.cursor()


def get_data():
    try:
        sql = "SELECT * FROM account"
        cur.execute(sql)
        rs = cur.fetchall()
        if not rs:
            print("Data empty!\n")
        else:
            print("=== Account info ===")
            print("ID\tAccount\tBalance")
            for row in rs:
                print("%s\t%s\t%d" % (row[0], row[1], row[2]))
            print("====================")
    except:
        conn.rollback()


def update_data(value):
    try:
        sql = "UPDATE `account` SET `balance`=%s WHERE `acc`=%s"
        # adr = tuple()  # ("accB", )
        cur.execute(sql, value)
        conn.commit()
        print("Update success!\n")
    except:
        conn.rollback()


while True:
    print("======= Menu =======")
    chose = int(input("1. Load data\n2. Update data\n3. Exit\nChoose: "))
    print("====================")
    if chose == 3:
        print("Exit!!\n")
        break
    elif chose == 1:
        get_data()
    elif chose == 2:
        name = input("Input acc: ")
        money = int(input("Input money: "))
        value = (money, name)
        update_data(value)
    else:
        print("Syntax error! Try again\n")
