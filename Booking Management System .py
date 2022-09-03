#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector 


# In[ ]:


connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="mysql")


# In[ ]:


import mysql.connector 
c=connection.cursor()
query1="create database kothari"
c.execute(query1)
query2="use kothari"
c.execute(query2)
query3="create table checkin (Day varchar(20),Name varchar(20),Aadhar integer(200),Date varchar(20),TypeNumber varchar(20))"
c.execute(query3)
query4=("create table checkout (TypeNumber varchar(20),Guest_num integer(20),fare integer(20),Day varchar(20),Total_bill integer(20),Date varchar(20))")
c.execute(query4)
connection.commit()


# In[ ]:



connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="mysql",
                                    database="kothari")   
def main():
    print("1. Check in")
    print("2. check out")
    print("3. Fare and Amenities")
    c=int(input("chioce:"))
    if c==1:
        checkin()
    elif c==2:
        checkout()
    elif c==3:
        rooms()
    else :
        print("Enter Correct Choice")
    
    main()
    
    
def checkin():
    a=input("Days:")
    b=input("Name:")
    c=input("Aadhar:")
    d=input("Date:")
    e=input("Type_and_Number:")
    data=(a,b,c,d,e)
    sql1=("insert into checkin values(%s,%s,%s,%s,%s)")
    c=connection.cursor()
    c.execute(sql1,data)
    print("Data Entered Successfully")
    main()
    
def checkout():
    f=input("Type_and_Number:")
    g=int(input("Guest_num:"))
    h=int(input("fare:"))
    i=int(input("Day:"))
    j=g*h*i
    k=input("Date:")
    data=(f,g,h,i,j,k)
    sql2=("insert into checkout values(%s,%s,%s,%s,%s,%s)")
    c=connection.cursor()
    c.execute(sql2,data)
    print("Data Entered Successfully")
    main()
    
def rooms():
    print("Executive - 5000Rs/d/g")
    print(" ")
    print("Facilities - WiFi , TV , AC , Bathroom with Tub and Geyser , Breakfast , Lunch , Dinner ")
    print(" ")
    print("Deluxe - 2000Rs/d/g")
    print(" ")
    print("Facilities - WiFi , TV , AC , Bathroom with Tub and Geyser ")
    print(" ")
    print("Simple - 1000Rs/d/g")
    print(" ")
    print("Facilities - WiFi , TV , Bathroom")
    main()

    
main()

