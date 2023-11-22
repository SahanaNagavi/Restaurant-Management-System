import sqlite3

conn=sqlite3.connect('resturant_.db')
c=conn.cursor()
print('connection success')
q="insert into restt values('steam momos','v',60,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('fried momos','v',90,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('tandoori momos','v',100,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('cheese momos','v',100,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('cheese corn momos','v',110,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('kothe momos','v',130,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('chicken momos','nv',150,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('fried chicken momos','nv',170,0,'momos')"
c.execute(q)
conn.commit()
q="insert into restt values('grilled chicken momos','nv',190,0,'momos')"
c.execute(q)
conn.commit()

q="insert into restt values('red sauce pasta','v',69,0,'pasta')"
c.execute(q)
conn.commit()
q="insert into restt values('white sauce pasta','v',69,0,'pasta')"
c.execute(q)
conn.commit()
q="insert into restt values('masala pasta','v',69,0,'pasta')"
c.execute(q)
conn.commit()
q="insert into restt values('carbonara','nv',150,0,'pasta')"
c.execute(q)
conn.commit()
q="insert into restt values('chicken piccata pasta','nv',170,0,'pasta')"
c.execute(q)
conn.commit()
q="insert into restt values('tasty kheema pasta','nv',185,0,'pasta')"
c.execute(q)
conn.commit()

q="insert into restt values('paneer tikka sizzler','v',200,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('mexican sizzler','v',230,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('thai sizzler','v',250,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('malpua rabri sizzler','v',270,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('chicken sizzler','nv',250,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('mutton sizzler','nv',300,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('fish sizzler','nv',250,0,'sizzler')"
c.execute(q)
conn.commit()
q="insert into restt values('prawn sizzler','nv',280,0,'sizzler')"
c.execute(q)
conn.commit()

q="insert into restt values('margherita pizza','v',200,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('italian pizza','v',230,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('american pizza','v',240,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('veggie pizza','v',230,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('pepperoni pizza','nv',350,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('meat pizza','nv',400,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('jerked chicken pizza','nv',400,0,'pizza')"
c.execute(q)
conn.commit()
q="insert into restt values('gamberi pizza','nv',450,0,'pizza')"
c.execute(q)
conn.commit()

q="insert into restt values('classic veggie burger','v',70,0,'burger')"
c.execute(q)
conn.commit()
q="insert into restt values('cheese burger','v',100,0,'burger')"
c.execute(q)
conn.commit()
q="insert into restt values('chilli burger','v',100,0,'burger')"
c.execute(q)
conn.commit()
q="insert into restt values('chicken burger','nv',200,0,'burger')"
c.execute(q)
conn.commit()
q="insert into restt values('butter-chicken burger','nv',230,0,'burger')"
c.execute(q)
conn.commit()
conn.close()

