from divar import Divar
import sqlite3 as DB
import logging

con = DB.connect("database.db")
cur = con.cursor()

divar = Divar()
divar.login("9199328173",cookie="sara.pkl")
posts = divar.all_posts("https://divar.ir/s/tehran/buy-apartment/doolab?districts=1017%2C273&user_type=personal")
posts = posts[:3]
c = 1

try:
    cur.execute("CREATE TABLE apartment_sell2(metraj, sakht, otagh, shomare, gheymat, gheymat_metr, agahi, tabaghe, toozihat)")
    print("made the table")
except:
    print("that table is already in DB")
for post in posts:
    res = divar.post_details(post)
    del res["شاخه"]
    val = tuple(v for v in res.values())
    print(val)
    cur.execute("INSERT INTO apartment_sell2 VALUES(?,?,?,?,?,?,?,?,?)", val)
    con.commit()
    print(c)
    c += 1

del divar