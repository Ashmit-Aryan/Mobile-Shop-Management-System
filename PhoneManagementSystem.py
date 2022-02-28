import sqlite3
from datetime import datetime

dbase = sqlite3.connect('contacts.db')
dbase.execute('CREATE TABLE IF NOT EXISTS' +
              '`CONTACT`(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,DATA TEXT,TIME_TODAY TEXT)')
cur = dbase.cursor()


def welcome():
    method = input("\nTo See all Info Enter 1 \n To Delete any Info Enter 2 \n To Enter a New Info Enter 3 \n To Search "
                   "a Particular Info Enter 4 \n")
    return str(method)


def check(id):
    cur.execute(f'select id from contact where id={id}')
    obj = cur.fetchone()
    if obj:
        return True
    else:
        return False


def valid_no(number):
    while True:
        if len(number) == 10 or len(number) == 8:
            return True
        else:
            return False


def new():
    name = input('Enter New Person Name \n').title()
    number = input('Enter New Phone Number \n')
    while True:
        if valid_no(number):
            break
        else:
            number = input('Enter New Phone Number')
    model = input('Enter New Phone Model \n')
    price = input('Enter New Phone Price \n')
    dop = input('Enter new Phone Date of Purchase \n')
    myDetail_List = [name, number, model, price, dop]
    cur.execute('INSERT INTO `CONTACT`(DATA,TIME_TODAY) VALUES(?,?)', (str(myDetail_List), datetime.now(),))
    print(f"\n New Phone Purchase Detail Entered \n id = {cur.lastrowid} ")
    dbase.commit()


def showAll():
    cur.execute('SELECT * FROM `CONTACT`')
    obj = cur.fetchall()
    if obj is None:
        print("\n No Data Exists")
    for i in obj:
        print(f'\nid:- {i[0]}')
        print(f'Name:- {eval(i[1])[0]}')
        print(f'Phone Number:- {eval(i[1])[1]}')
        print(f'Phone Model:- {eval(i[1])[2]}')
        print(f'Phone Price:- {eval(i[1])[3]}')
        print(f'Phone Date Of Purchase:- {eval(i[1])[4]}')
    dbase.commit()


def delete(id):
    if check(id):
        cur.execute(f'delete from contact where id={id}')
        print("Delete successful")
    else:
        print(f"No such info exist")
    dbase.commit()


def search(id):
    cur.execute(f'select DATA , id from contact where id={id}')
    obj = cur.fetchone()
    if obj:
        print(f'\nid:- {obj[1]}')
        print(f'Name:- {eval(obj[0])[0]}')
        print(f'Phone Number:- {eval(obj[0])[1]}')
        print(f'Phone Model:- {eval(obj[0])[2]}')
        print(f'Phone Price:- {eval(obj[0])[3]}')
        print(f'Phone Date Of Purchase:- {eval(obj[0])[4]}')
    else:
        print(f"No such info exist")
    dbase.commit()

def main():
    while True:
        method = welcome()
        if method == '1':
            showAll()
        elif method == '2':
            id = input("Enter id To Delete")
            delete(id)
        elif method == '3':
            new()
        elif method == '4':
            id = input("Enter id To Search")
            search(id)

if __name__ == '__main__':
    main()
