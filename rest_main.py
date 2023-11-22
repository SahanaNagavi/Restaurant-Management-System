import sqlite3
from tkinter import *
             
class menu_:
    def __init__(self,root,f):
        
        self.l0=Label(f,text="MENU",font=('courier',20,'bold','underline'))
        self.l0.place(x=1130,y=50)
        q1="select food,price,food_type from restt"
        c.execute(q1)
        r1=c.fetchall()
        
        #momos
        self.momos=Label(f,text="MOMOS",font=('courier',15,'bold'))
        self.momos.place(x=900,y=110)
        yco=140
        yco1=140
        for i in r1: 
            if i[2]=='momos':
                self.l1=Label(f,text=i[0],font=('courier',12))
                self.l1.place(x=900,y=yco)
                yco=yco+20
                self.l2=Label(f,text=i[1],font=('courier',12))
                self.l2.place(x=1130,y=yco1)
                yco1=yco1+20
                
        #pasta
        self.pasta=Label(f,text="PASTA",font=('courier',15,'bold'))
        self.pasta.place(x=900,y=350)
        yco=380
        yco1=380
        for i in r1: 
            if i[2]=='pasta':
                self.l1=Label(f,text=i[0],font=('courier',12))
                self.l1.place(x=900,y=yco)
                yco=yco+20
                self.l2=Label(f,text=i[1],font=('courier',12))
                self.l2.place(x=1130,y=yco1)
                yco1=yco1+20
                
        #sizzler
        self.sizzler=Label(f,text="SIZZLER",font=('courier',15,'bold'))
        self.sizzler.place(x=900,y=520)
        yco=550
        yco1=550
        for i in r1: 
            if i[2]=='sizzler':
                self.l1=Label(f,text=i[0],font=('courier',12))
                self.l1.place(x=900,y=yco)
                yco=yco+20
                self.l2=Label(f,text=i[1],font=('courier',12))
                self.l2.place(x=1130,y=yco1)
                yco1=yco1+20
                
        #pizza
        self.pizza=Label(f,text="PIZZA",font=('courier',15,'bold'))
        self.pizza.place(x=1190,y=110)
        yco=140
        yco1=140
        for i in r1: 
            if i[2]=='pizza':
                self.l1=Label(f,text=i[0],font=('courier',12))
                self.l1.place(x=1190,y=yco)
                yco=yco+20
                self.l2=Label(f,text=i[1],font=('courier',12))
                self.l2.place(x=1420,y=yco1)
                yco1=yco1+20
                
        #burger
        self.burger=Label(f,text="BURGER",font=('courier',15,'bold'))
        self.burger.place(x=1190,y=350)
        yco=380
        yco1=380
        for i in r1: 
            if i[2]=='burger':
                self.l1=Label(f,text=i[0],font=('courier',12))
                self.l1.place(x=1190,y=yco)
                yco=yco+20
                self.l2=Label(f,text=i[1],font=('courier',12))
                self.l2.place(x=1420,y=yco1)
                yco1=yco1+20

class spin_:
    
    def __init__(self,root,f):
        self.l0=Label(f,text="ORDER HERE",font=('courier',20,'bold','underline'))
        self.l0.place(x=300,y=50)
        
        #momos
        self.momos=Label(f,text="MOMOS",font=('courier',15,'bold'))
        self.momos.place(x=100,y=110)
        q="select * from restt where food_type='momos'"
        c.execute(q)
        r=c.fetchall()
        food=[]
        for i in r:
            food.append(i[0])    
        self.s1m=Spinbox(f,width=25,values=food)
        self.s1m.place(x=100,y=140)
        self.s2m=Spinbox(f,width=10,from_=0,to=10)
        self.s2m.place(x=270,y=140)
        self.s3m=Spinbox(f,width=25,values=food)
        self.s3m.place(x=100,y=170)
        self.s4m=Spinbox(f,width=10,from_=0,to=10)
        self.s4m.place(x=270,y=170)
        self.s5m=Spinbox(f,width=25,values=food)
        self.s5m.place(x=100,y=200)
        self.s6m=Spinbox(f,width=10,from_=0,to=10)
        self.s6m.place(x=270,y=200)
        
        #pasta
        self.pasta=Label(f,text="PASTA",font=('courier',15,'bold'))
        self.pasta.place(x=100,y=230)
        q="select * from restt where food_type='pasta'"
        c.execute(q)
        r=c.fetchall()
        food=[]
        for i in r:
            food.append(i[0])    
        self.s1p=Spinbox(f,width=25,values=food)
        self.s1p.place(x=100,y=260)
        self.s2p=Spinbox(f,width=10,from_=0,to=10)
        self.s2p.place(x=270,y=260)
        self.s3p=Spinbox(f,width=25,values=food)
        self.s3p.place(x=100,y=290)
        self.s4p=Spinbox(f,width=10,from_=0,to=10)
        self.s4p.place(x=270,y=290)
        self.s5p=Spinbox(f,width=25,values=food)
        self.s5p.place(x=100,y=320)
        self.s6p=Spinbox(f,width=10,from_=0,to=10)
        self.s6p.place(x=270,y=320)
        
        #sizzler
        self.sizzler=Label(f,text="SIZZLER",font=('courier',15,'bold'))
        self.sizzler.place(x=100,y=350)
        q="select * from restt where food_type='sizzler'"
        c.execute(q)
        r=c.fetchall()
        food=[]
        for i in r:
            food.append(i[0])    
        self.s1s=Spinbox(f,width=25,values=food)
        self.s1s.place(x=100,y=380)
        self.s2s=Spinbox(f,width=10,from_=0,to=10)
        self.s2s.place(x=270,y=380)
        self.s3s=Spinbox(f,width=25,values=food)
        self.s3s.place(x=100,y=410)
        self.s4s=Spinbox(f,width=10,from_=0,to=10)
        self.s4s.place(x=270,y=410)
        self.s5s=Spinbox(f,width=25,values=food)
        self.s5s.place(x=100,y=440)
        self.s6s=Spinbox(f,width=10,from_=0,to=10)
        self.s6s.place(x=270,y=440)
        
        #pizza
        self.pizza=Label(f,text="PIZZA",font=('courier',15,'bold'))
        self.pizza.place(x=460,y=110)
        q="select * from restt where food_type='pizza'"
        c.execute(q)
        r=c.fetchall()
        food=[]
        for i in r:
            food.append(i[0])    
        self.s1pi=Spinbox(f,width=25,values=food)
        self.s1pi.place(x=460,y=140)
        self.s2pi=Spinbox(f,width=10,from_=0,to=10)
        self.s2pi.place(x=630,y=140)
        self.s3pi=Spinbox(f,width=25,values=food)
        self.s3pi.place(x=460,y=170)
        self.s4pi=Spinbox(f,width=10,from_=0,to=10)
        self.s4pi.place(x=630,y=170)
        self.s5pi=Spinbox(f,width=25,values=food)
        self.s5pi.place(x=460,y=200)
        self.s6pi=Spinbox(f,width=10,from_=0,to=10)
        self.s6pi.place(x=630,y=200)
        
        #burger
        self.burger=Label(f,text="BURGER",font=('courier',15,'bold'))
        self.burger.place(x=460,y=230)
        q="select * from restt where food_type='burger'"
        c.execute(q)
        r=c.fetchall()
        food=[]
        for i in r:
            food.append(i[0])    
        self.s1b=Spinbox(f,width=25,values=food)
        self.s1b.place(x=460,y=260)
        self.s2b=Spinbox(f,width=10,from_=0,to=10)
        self.s2b.place(x=630,y=260)
        self.s3b=Spinbox(f,width=25,values=food)
        self.s3b.place(x=460,y=290)
        self.s4b=Spinbox(f,width=10,from_=0,to=10)
        self.s4b.place(x=630,y=290)
        self.s5b=Spinbox(f,width=25,values=food)
        self.s5b.place(x=460,y=320)
        self.s6b=Spinbox(f,width=10,from_=0,to=10)
        self.s6b.place(x=630,y=320)
        
        #order button
        self.b1=Button(f,text="ORDER",command=self.bill,font=('courier',15,'bold'))
        self.b1.place(x=535,y=395)
        
    def bill(self):
        
        #momos
        fd1m=self.s1m.get()
        quan1m=self.s2m.get()
        fd2m=self.s3m.get()
        quan2m=self.s4m.get()
        fd3m=self.s5m.get()
        quan3m=self.s6m.get()
        
        #pasta
        fd1p=self.s1p.get()
        quan1p=self.s2p.get()
        fd2p=self.s3p.get()
        quan2p=self.s4p.get()
        fd3p=self.s5p.get()
        quan3p=self.s6p.get()
        
        #sizzler
        fd1s=self.s1s.get()
        quan1s=self.s2s.get()
        fd2s=self.s3s.get()
        quan2s=self.s4s.get()
        fd3s=self.s5s.get()
        quan3s=self.s6s.get()
        
        #pizza
        fd1pi=self.s1pi.get()
        quan1pi=self.s2pi.get()
        fd2pi=self.s3pi.get()
        quan2pi=self.s4pi.get()
        fd3pi=self.s5pi.get()
        quan3pi=self.s6pi.get()
        
        #burger
        fd1b=self.s1b.get()
        quan1b=self.s2b.get()
        fd2b=self.s3b.get()
        quan2b=self.s4b.get()
        fd3b=self.s5b.get()
        quan3b=self.s6b.get()
        
        #BILLING
        self.bill=Label(f,text="BILLING",font=('courier',20,'bold','underline'))
        self.bill.place(x=330,y=470)
        
        self.item=Label(f,text="ITEM",font=('courier',15,'bold'))
        self.item.place(x=100,y=520)
        self.quan=Label(f,text="QUANTITY",font=('courier',15,'bold'))
        self.quan.place(x=330,y=520)
        self.price=Label(f,text="PRICE",font=('courier',15,'bold'))
        self.price.place(x=600,y=520)
        
        #INTIALIZE
        price1_momo,price2_momo,price3_momo=0,0,0
        price1_pasta,price2_pasta,price3_pasta=0,0,0
        price1_sizz,price2_sizz,price3_sizz=0,0,0
        price1_pizza,price2_pizza,price3_pizza=0,0,0
        price1_burg,price2_burg,price3_burg=0,0,0
        
        #MOMOS
        c.execute('select price from restt where food=?',[fd1m])
        r1=c.fetchall()
        c.execute('select price from restt where food=?',[fd2m])
        r2=c.fetchall()
        c.execute('select price from restt where food=?',[fd3m])
        r3=c.fetchall()
        
        if int(quan1m)!=0 and int(quan2m)==0 and int(quan3m)==0:
            
            self.momo1_item=Label(f,text=fd1m,font=('courier',12))
            self.momo1_item.place(x=100,y=560)
            self.momo1_quan=Label(f,text=quan1m,font=('courier',12))
            self.momo1_quan.place(x=330,y=560)
            for i in r1:
                rr1 = i[0]
            price1_momo=rr1*int(quan1m)
            self.momo1=Label(f,text=str(price1_momo),font=('courier',12))
            self.momo1.place(x=630,y=560)
            
            
        if int(quan1m)!=0 and int(quan2m)!=0 and int(quan3m)==0:
            
            self.momo1_item=Label(f,text=fd1m,font=('courier',12))
            self.momo1_item.place(x=100,y=560)
            self.momo1_quan=Label(f,text=quan1m,font=('courier',12))
            self.momo1_quan.place(x=330,y=560)
            for i in r1:
                rr1 = i[0]
            price1_momo=rr1*int(quan1m)
            self.momo1=Label(f,text=str(price1_momo),font=('courier',12))
            self.momo1.place(x=630,y=560)
            
            
            self.momo2_item=Label(f,text=fd2m,font=('courier',12))
            self.momo2_item.place(x=100,y=580)
            self.momo2_quan=Label(f,text=quan2m,font=('courier',12))
            self.momo2_quan.place(x=330,y=580)
            for i in r2:
                rr2 = i[0]
            price2_momo=rr2*int(quan2m)
            self.momo2=Label(f,text=str(price2_momo),font=('courier',12))
            self.momo2.place(x=630,y=580)
            
            
            
        if int(quan1m)!=0 and int(quan2m)!=0 and int(quan3m)!=0:
            
            self.momo1_item=Label(f,text=fd1m,font=('courier',12))
            self.momo1_item.place(x=100,y=560)
            self.momo1_quan=Label(f,text=quan1m,font=('courier',12))
            self.momo1_quan.place(x=330,y=560)
            for i in r1:
                rr1 = i[0]
            price1_momo=rr1*int(quan1m)
            self.momo1=Label(f,text=str(price1_momo),font=('courier',12))
            self.momo1.place(x=630,y=560)
            
            
            self.momo2_item=Label(f,text=fd2m,font=('courier',12))
            self.momo2_item.place(x=100,y=580)
            self.momo2_quan=Label(f,text=quan2m,font=('courier',12))
            self.momo2_quan.place(x=330,y=580)
            for i in r2:
                rr2 = i[0]
            price2_momo=rr2*int(quan2m)
            self.momo2=Label(f,text=str(price2_momo),font=('courier',12))
            self.momo2.place(x=630,y=580)
            
            self.momo3_item=Label(f,text=fd3m,font=('courier',12))
            self.momo3_item.place(x=100,y=600)
            self.momo3_quan=Label(f,text=quan3m,font=('courier',12))
            self.momo3_quan.place(x=330,y=600)
            for i in r3:
                rr3 = i[0]
            price3_momo=rr3*int(quan3m)
            self.momo3=Label(f,text=str(price3_momo),font=('courier',12))
            self.momo3.place(x=630,y=600)
            
        
        #PASTA
        c.execute('select price from restt where food=?',[fd1p])
        r1=c.fetchall()
        c.execute('select price from restt where food=?',[fd2p])
        r2=c.fetchall()
        c.execute('select price from restt where food=?',[fd3p])
        r3=c.fetchall()
        
        if int(quan1p)!=0 and int(quan2p)==0 and int(quan3p)==0:
            
            self.pasta1_item=Label(f,text=fd1p,font=('courier',12))
            self.pasta1_item.place(x=100,y=620)
            self.pasta1_quan=Label(f,text=quan1p,font=('courier',12))
            self.pasta1_quan.place(x=330,y=620)
            for i in r1:
                rr1 = i[0]
            price1_pasta=rr1*int(quan1p)
            self.pasta1=Label(f,text=str(price1_pasta),font=('courier',12))
            self.pasta1.place(x=630,y=620)
            
            
        if int(quan1p)!=0 and int(quan2p)!=0 and int(quan3p)==0:
           
            self.pasta1_item=Label(f,text=fd1p,font=('courier',12))
            self.pasta1_item.place(x=100,y=620)
            self.pasta1_quan=Label(f,text=quan1p,font=('courier',12))
            self.pasta1_quan.place(x=330,y=620)
            for i in r1:
                rr1 = i[0]
            price1_pasta=rr1*int(quan1p)
            self.pasta1=Label(f,text=str(price1_pasta),font=('courier',12))
            self.pasta1.place(x=630,y=620)
            
            
            self.pasta2_item=Label(f,text=fd2p,font=('courier',12))
            self.pasta2_item.place(x=100,y=640)
            self.pasta2_quan=Label(f,text=quan2p,font=('courier',12))
            self.pasta2_quan.place(x=330,y=640)
            for i in r2:
                rr2 = i[0]
            price2_pasta=rr2*int(quan2p)
            self.pasta2=Label(f,text=str(price2_pasta),font=('courier',12))
            self.pasta2.place(x=630,y=640)
            
            
            
        if int(quan1p)!=0 and int(quan2p)!=0 and int(quan3p)!=0:
            
            self.pasta1_item=Label(f,text=fd1p,font=('courier',12))
            self.pasta1_item.place(x=100,y=620)
            self.pasta1_quan=Label(f,text=quan1p,font=('courier',12))
            self.pasta1_quan.place(x=330,y=620)
            for i in r1:
                rr1 = i[0]
            price1_pasta=rr1*int(quan1p)
            self.pasta1=Label(f,text=str(price1_pasta),font=('courier',12))
            self.pasta1.place(x=630,y=620)
            
            
            self.pasta2_item=Label(f,text=fd2p,font=('courier',12))
            self.pasta2_item.place(x=100,y=640)
            self.pasta2_quan=Label(f,text=quan2p,font=('courier',12))
            self.pasta2_quan.place(x=330,y=640)
            for i in r2:
                rr2 = i[0]
            price2_pasta=rr2*int(quan2p)
            self.pasta2=Label(f,text=str(price2_pasta),font=('courier',12))
            self.pasta2.place(x=630,y=640)
            
            self.pasta3_item=Label(f,text=fd3p,font=('courier',12))
            self.pasta3_item.place(x=100,y=660)
            self.pasta3_quan=Label(f,text=quan3p,font=('courier',12))
            self.pasta3_quan.place(x=330,y=660)
            for i in r3:
                rr3 = i[0]
            price3_pasta=rr3*int(quan3p)
            self.pasta3=Label(f,text=str(price3_pasta),font=('courier',12))
            self.pasta3.place(x=630,y=660)
            
        #SIZZLER
        c.execute('select price from restt where food=?',[fd1s])
        r1=c.fetchall()
        c.execute('select price from restt where food=?',[fd2s])
        r2=c.fetchall()
        c.execute('select price from restt where food=?',[fd3s])
        r3=c.fetchall()
        
        if int(quan1s)!=0 and int(quan2s)==0 and int(quan3s)==0:
            
            self.sizz1_item=Label(f,text=fd1s,font=('courier',12))
            self.sizz1_item.place(x=100,y=680)
            self.sizz1_quan=Label(f,text=quan1s,font=('courier',12))
            self.sizz1_quan.place(x=330,y=680)
            for i in r1:
                rr1 = i[0]
            price1_sizz=rr1*int(quan1s)
            self.sizz1=Label(f,text=str(price1_sizz),font=('courier',12))
            self.sizz1.place(x=630,y=680)
            
            
        if int(quan1s)!=0 and int(quan2s)!=0 and int(quan3s)==0:
           
            self.sizz1_item=Label(f,text=fd1s,font=('courier',12))
            self.sizz1_item.place(x=100,y=680)
            self.sizz1_quan=Label(f,text=quan1s,font=('courier',12))
            self.sizz1_quan.place(x=330,y=680)
            for i in r1:
                rr1 = i[0]
            price1_sizz=rr1*int(quan1s)
            self.sizz1=Label(f,text=str(price1_sizz),font=('courier',12))
            self.sizz1.place(x=630,y=680)
            
            
            self.sizz2_item=Label(f,text=fd2s,font=('courier',12))
            self.sizz2_item.place(x=100,y=700)
            self.sizz2_quan=Label(f,text=quan2s,font=('courier',12))
            self.sizz2_quan.place(x=330,y=700)
            for i in r2:
                rr2 = i[0]
            price2_sizz=rr2*int(quan2s)
            self.sizz2=Label(f,text=str(price2_sizz),font=('courier',12))
            self.sizz2.place(x=630,y=700)
            
            
            
        if int(quan1s)!=0 and int(quan2s)!=0 and int(quan3s)!=0:
            
            self.sizz1_item=Label(f,text=fd1s,font=('courier',12))
            self.sizz1_item.place(x=100,y=680)
            self.sizz1_quan=Label(f,text=quan1s,font=('courier',12))
            self.sizz1_quan.place(x=330,y=680)
            for i in r1:
                rr1 = i[0]
            price1_sizz=rr1*int(quan1s)
            self.sizz1=Label(f,text=str(price1_sizz),font=('courier',12))
            self.sizz1.place(x=630,y=680)
            
            
            self.sizz2_item=Label(f,text=fd2s,font=('courier',12))
            self.sizz2_item.place(x=100,y=700)
            self.sizz2_quan=Label(f,text=quan2s,font=('courier',12))
            self.sizz2_quan.place(x=330,y=700)
            for i in r2:
                rr2 = i[0]
            price2_sizz=rr2*int(quan2s)
            self.sizz2=Label(f,text=str(price2_sizz),font=('courier',12))
            self.sizz2.place(x=630,y=700)
            
            self.sizz3_item=Label(f,text=fd3s,font=('courier',12))
            self.sizz3_item.place(x=100,y=720)
            self.sizz3_quan=Label(f,text=quan3s,font=('courier',12))
            self.sizz3_quan.place(x=330,y=720)
            for i in r3:
                rr3 = i[0]
            price3_sizz=rr3*int(quan3s)
            self.sizz3=Label(f,text=str(price3_sizz),font=('courier',12))
            self.sizz3.place(x=630,y=720)
        
        #PIZZA
        c.execute('select price from restt where food=?',[fd1pi])
        r1=c.fetchall()
        c.execute('select price from restt where food=?',[fd2pi])
        r2=c.fetchall()
        c.execute('select price from restt where food=?',[fd3pi])
        r3=c.fetchall()
        
        if int(quan1pi)!=0 and int(quan2pi)==0 and int(quan3pi)==0:
            
            self.pizza1_item=Label(f,text=fd1pi,font=('courier',12))
            self.pizza1_item.place(x=100,y=740)
            self.pizza1_quan=Label(f,text=quan1pi,font=('courier',12))
            self.pizza1_quan.place(x=330,y=740)
            for i in r1:
                rr1 = i[0]
            price1_pizza=rr1*int(quan1pi)
            self.pizza1=Label(f,text=str(price1_pizza),font=('courier',12))
            self.pizza1.place(x=630,y=740)
            
            
        if int(quan1pi)!=0 and int(quan2pi)!=0 and int(quan3pi)==0:
           
           self.pizza1_item=Label(f,text=fd1pi,font=('courier',12))
           self.pizza1_item.place(x=100,y=740)
           self.pizza1_quan=Label(f,text=quan1pi,font=('courier',12))
           self.pizza1_quan.place(x=330,y=740)
           for i in r1:
               rr1 = i[0]
           price1_pizza=rr1*int(quan1pi)
           self.pizza1=Label(f,text=str(price1_pizza),font=('courier',12))
           self.pizza1.place(x=630,y=740)
           
           self.pizza2_item=Label(f,text=fd2pi,font=('courier',12))
           self.pizza2_item.place(x=100,y=760)
           self.pizza2_quan=Label(f,text=quan2pi,font=('courier',12))
           self.pizza2_quan.place(x=330,y=760)
           for i in r2:
               rr2 = i[0]
           price2_pizza=rr2*int(quan2pi)
           self.pizza2=Label(f,text=str(price2_pizza),font=('courier',12))
           self.pizza2.place(x=630,y=760)

            
            
        if int(quan1pi)!=0 and int(quan2pi)!=0 and int(quan3pi)!=0:
            
            self.pizza1_item=Label(f,text=fd1pi,font=('courier',12))
            self.pizza1_item.place(x=100,y=740)
            self.pizza1_quan=Label(f,text=quan1pi,font=('courier',12))
            self.pizza1_quan.place(x=330,y=740)
            for i in r1:
                rr1 = i[0]
            price1_pizza=rr1*int(quan1pi)
            self.pizza1=Label(f,text=str(price1_pizza),font=('courier',12))
            self.pizza1.place(x=630,y=740)
            
            self.pizza2_item=Label(f,text=fd2pi,font=('courier',12))
            self.pizza2_item.place(x=100,y=760)
            self.pizza2_quan=Label(f,text=quan2pi,font=('courier',12))
            self.pizza2_quan.place(x=330,y=760)
            for i in r2:
                rr2 = i[0]
            price2_pizza=rr2*int(quan2pi)
            self.pizza2=Label(f,text=str(price2_pizza),font=('courier',12))
            self.pizza2.place(x=630,y=760)
            
            self.pizza3_item=Label(f,text=fd3pi,font=('courier',12))
            self.pizza3_item.place(x=100,y=780)
            self.pizza3_quan=Label(f,text=quan3pi,font=('courier',12))
            self.pizza3_quan.place(x=330,y=780)
            for i in r3:
                rr3 = i[0]
            price3_pizza=rr3*int(quan3pi)
            self.pizza3=Label(f,text=str(price3_pizza),font=('courier',12))
            self.pizza3.place(x=630,y=780)
            
        #BURGER
        c.execute('select price from restt where food=?',[fd1b])
        r1=c.fetchall()
        c.execute('select price from restt where food=?',[fd2b])
        r2=c.fetchall()
        c.execute('select price from restt where food=?',[fd3b])
        r3=c.fetchall()
        
        if int(quan1b)!=0 and int(quan2b)==0 and int(quan3b)==0:
            
            self.burg1_item=Label(f,text=fd1b,font=('courier',12))
            self.burg1_item.place(x=100,y=800)
            self.burg1_quan=Label(f,text=quan1b,font=('courier',12))
            self.burg1_quan.place(x=330,y=800)
            for i in r1:
                rr1 = i[0]
            price1_burg=rr1*int(quan1b)
            self.burg1=Label(f,text=str(price1_burg),font=('courier',12))
            self.burg1.place(x=630,y=800)
            
            
        if int(quan1b)!=0 and int(quan2b)!=0 and int(quan3b)==0:
           
           self.burg1_item=Label(f,text=fd1b,font=('courier',12))
           self.burg1_item.place(x=100,y=800)
           self.burg1_quan=Label(f,text=quan1b,font=('courier',12))
           self.burg1_quan.place(x=330,y=800)
           for i in r1:
               rr1 = i[0]
           price1_burg=rr1*int(quan1b)
           self.burg1=Label(f,text=str(price1_burg),font=('courier',12))
           self.burg1.place(x=630,y=800)
           
           self.burg2_item=Label(f,text=fd2b,font=('courier',12))
           self.burg2_item.place(x=100,y=820)
           self.burg2_quan=Label(f,text=quan2b,font=('courier',12))
           self.burg2_quan.place(x=330,y=820)
           for i in r2:
               rr2 = i[0]
           price2_burg=rr2*int(quan2b)
           self.burg2=Label(f,text=str(price2_burg),font=('courier',12))
           self.burg2.place(x=630,y=820)

            
            
        if int(quan1b)!=0 and int(quan2b)!=0 and int(quan3b)!=0:
            
            self.burg1_item=Label(f,text=fd1b,font=('courier',12))
            self.burg1_item.place(x=100,y=800)
            self.burg1_quan=Label(f,text=quan1b,font=('courier',12))
            self.burg1_quan.place(x=330,y=800)
            for i in r1:
                rr1 = i[0]
            price1_burg=rr1*int(quan1b)
            self.burg1=Label(f,text=str(price1_burg),font=('courier',12))
            self.burg1.place(x=630,y=800)
            
            self.burg2_item=Label(f,text=fd2b,font=('courier',12))
            self.burg2_item.place(x=100,y=820)
            self.burg2_quan=Label(f,text=quan2b,font=('courier',12))
            self.burg2_quan.place(x=330,y=820)
            for i in r2:
                rr2 = i[0]
            price2_burg=rr2*int(quan2b)
            self.burg2=Label(f,text=str(price2_burg),font=('courier',12))
            self.burg2.place(x=630,y=820)
            
            self.burg3_item=Label(f,text=fd3b,font=('courier',12))
            self.burg3_item.place(x=100,y=840)
            self.burg3_quan=Label(f,text=quan3b,font=('courier',12))
            self.burg3_quan.place(x=330,y=840)
            for i in r3:
                rr3 = i[0]
            price3_burg=rr3*int(quan3b)
            self.burg3=Label(f,text=str(price3_burg),font=('courier',12))
            self.burg3.place(x=630,y=840)
        
        #TOTAL CALCULATION
        self.total=Label(f,text="TOTAL",font=('courier',15,'bold'))
        self.total.place(x=330,y=870)
        sum=price1_momo+price2_momo+price3_momo+price1_pasta+price2_pasta+price3_pasta+price1_sizz+price2_sizz+price3_sizz+price1_pizza+price2_pizza+price3_pizza+price1_burg+price2_burg+price3_burg
        self.sum=Label(f,text=str(sum),font=('courier',15,'bold'))
        self.sum.place(x=630,y=870)
        

root=Tk()
root.title('resturant')
#connection
conn=sqlite3.connect('resturant_.db')
c=conn.cursor()

f=Frame(root,height=950,width=1500)
f.propagate(0)
f.pack()
head=Label(f,text="THE CHILL GRILL",font=('courier',30,'bold'))
head.place(x=550,y=10)
b=menu_(root,f)
a=spin_(root,f)

root.mainloop()

