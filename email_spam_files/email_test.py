# -*- coding: UTF-8 -*-
import sqlite3

conn=sqlite3.connect("spam.db")
cur=conn.cursor()

#Following lines were alternately commented for testing the desired files
fh=open("smail_test.txt","r")
#fh=open("nmail_test.txt","r")

ds=[]
dn=[]
w=[]
v=[]
cur.execute("select spam_value,non_spam_value,weight from email_spam_train_data order by id")
n=0
fs=0
ts=0
row=cur.fetchall()
for r in row:
    ds.append(r[0])
    dn.append(r[1])
    w.append(r[2])


for line in fh:
    n=n+1
    da=line.split(",")
    del da[-1]
    i=0

    for i in range(len(da)):

        if abs(float(da[i])-ds[i])>abs(float(da[i])-dn[i]):
                v.append(w[i]*1)
        
        else:
            v.append(w[i]*-1)


    count=0
    value=0

    for count in range(len(v)):
        value=value+v[count]
        count=count+1

    if value<0:
        fs=fs+1

    else:
        ts=ts+1

    del v[:]

per_nspam=round((float(ts)/float(n))*100,2)
per_spam=round((float(fs)/float(n))*100,2)

print "Total Number of emails=",n
print "Spam mails=",fs," % Spam=",per_spam
print "Non Spam mails=",ts," %Non Spam=",per_nspam
        
        

