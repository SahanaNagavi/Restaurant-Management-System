import sqlite3
try:
    conn=sqlite3.connect('resturant_.db')
    c=conn.cursor()
    q="create table restt(food varchar(30),type varchar(2),price int,quantity int,food_type varchar(30))"
    c.execute(q)
except Exception as e:
    print(e)
    
    