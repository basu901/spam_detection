import sqlite3
import os

conn=sqlite3.connect("spam.db")
cur=conn.cursor()
fh=open('email_train_data.js','w')

fh.write("email_train_data=[['Parameter','Non Spam Value','Spam Value','Exponent'],")

cur.execute('''SELECT parameter,spam_value,non_spam_value FROM email_spam_train_data''')
rows=cur.fetchall()
ex=0
for row in rows:
    s=row[0]
    val=s[:-1]
    if row[1]<float(1):
        s_val=round(row[1]*100,2)
        n_val=round(row[2]*100,2)
        ex=-2
    elif row[1]<float(10):
        s_val=round(row[1]*10,2)
        n_val=round(row[2]*10,2)
        ex=-1

    elif row[1]>100:
        s_val=round(row[1]/10,2)
        n_val=round(row[2]/10,2)
        ex=1
    else:
        s_val=round(row[1],2)
        n_val=round(row[2],2)
        ex=0
        
    fh.write("['"+val+"',"+str(n_val)+","+str(s_val)+","+str(ex)+"],\n")
    
fh.seek(-1,os.SEEK_END)
fh.truncate()

fh.write("]")
fh.close()

