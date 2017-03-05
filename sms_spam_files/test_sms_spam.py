# -*- coding: UTF-8 -*-
#used for testing the data, after training
import sqlite3
from decimal import *
import sys  

def one(line,w1):
    total=Decimal(0)
    count=0
    count_total_words=0
    words=line.split()
    del words[0]
    for word in words:
            if word.lower().find(w1)>-1:
                count=count+1
                count_total_words=count_total_words+1
            else:
                count_total_words=count_total_words+1
    try:
        total=Decimal(count)/Decimal(count_total_words)
    except:
        total=Decimal(0)

    return round(total,6)


def special(line,s):
    total=Decimal(0)
    count=0
    count_total_char=0
    words=line.split()
    del words[0]
    for word in words:
         for ch in word:
             if ch==s:
                 count=count+1
                 count_total_char=count_total_char+1
             else:
                 count_total_char=count_total_char+1

    try:
        total=Decimal(count)/Decimal(count_total_char)
    except:
        total=Decimal(0)

    return round(total,6)
                    

def digits(line):
    pro=Decimal(0)
    count=0
    words=line.split()
    del words[0]
    for word in words:
        for ch in word:
            try:
                check=int(ch)
                count=count+1
            except:
                continue

    pro=Decimal(count)
    return round(pro,6)
            

def dig_avg_len(line):
    length_count=0
    avg_per_line=Decimal(0)
    count=0
    words=line.split()
    del words[0]
    for word in words:
         try:
             check=int(word)
             length_count=length_count+len(word)
             count=count+1
         except:
              continue

    if count>0:
         avg_per_line=Decimal(length_count)/Decimal(count)
    else:
         avg_per_line=Decimal(0)
        
    return round(avg_per_line,6)  


def lower(line):
    low=Decimal(0)
    count=0
    count_total_words=0
    words=line.split()
    del words[0]
    for word in words:
        if word.islower():
            count=count+1
            count_total_words=count_total_words+1
        else:
            count_total_words=count_total_words+1

    try:
        low=Decimal(count)/Decimal(count_total_words)
    except:
        low=Decimal(0)
    return round(low,6)


def mixed(line):
    mix=Decimal(0)
    count=0
    count_total_words=0
    words=line.split()
    del words[0]
    for word in words:
        if not word.islower() and not word.isupper():
            count=count+1
            count_total_words=count_total_words+1
        else:
            count_total_words=count_total_words+1

    try:
        mix=Decimal(count)/Decimal(count_total_words)
    except:
        mix=Decimal(0)

    return round(mix,6)


def i_count(line):
    icount=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_word=0
    words=line.split()
    del words[0]
    for word in words:
        if word.lower().find('i')>-1 or word.lower().find("i\'")>-1:
                    if len(word)<5:
                        count=count+1
                        count_total_word=count_total_word+1
                    else:
                        count_total_word=count_total_word+1
        else:
            count_total_word=count_total_word+1

    try:
        icount=Decimal(count)/Decimal(count_total_words)
    except:
        icount=Decimal(0)

    return round(icount,6)


def upper(line):
    up=Decimal(0)
    count=0
    count_total_words=0
    words=line.split()
    del words[0]
    for word in words:
            if word.isupper():
                count=count+1
                count_total_words=count_total_words+1
            else:
                count_total_words=count_total_words+1

    try:
        up=Decimal(count)/Decimal(count_total_words)
    except:
        up=Decimal(0)
    return round(up,6)



def two_combined(line,w1,w2):
    total=Decimal(0)
    count=0
    count_total_words=0
    count1=0
    count2=0
    words=line.split()
    del words[0]
    for word in words:
            if word.lower().find(w1)>-1:
                count1=count1+1
                count_total_words=count_total_words+1

            elif word.lower().find(w2)>-1:
                count2=count2+1
                count_total_words=count_total_words+1
                    
            else:
                count_total_words=count_total_words+1

        
    if count1>0 and count2>0:
        count=count1+count2

            
    try:
        total=Decimal(count)/Decimal(count_total_words)
    except:
        total=Decimal(0)

    return round(total,6)


def two_similar(line,w1,w2):
    total=Decimal(0)
    count=0
    count_total_words=0
    words=line.split()
    del words[0]
    for word in words:
            if word.lower().find(w1)>-1 or word.lower().find(w2)>-1:
                count=count+1
                count_total_words=count_total_words+1
                    
            else:
                count_total_words=count_total_words+1

            
    try:
        total=Decimal(count)/Decimal(count_total_words)
    except:
        total=Decimal(0)

    return round(total,6)



def check_spam_sms(filename):
    
    conn=sqlite3.connect("spam.db")
    cur=conn.cursor()
    spam=0
    n_spam=0
    fh=open(filename,'r')
    for l in fh:
        w=l.split()
        del w[0]
        line=' '.join(w)
        total=float(0)
        cur.execute('''SELECT id,parameter from sms_spam''')
        rows=cur.fetchall()
        for row in rows:
            param=row[1].strip()
            p_id=row[0]
            if param.find(",")>-1:
                words=param.split(",")
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=two_similar(unicode(line),unicode(words[0].strip()),unicode(words[1].strip()))
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)
                    
            elif param.find("+")>-1:
                words=param.split("+")
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=two_combined(unicode(line),unicode(words[0].strip()),unicode(words[1].strip()))
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)
       

            elif param.find("i")>-1 and len(param)<3:
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=i_count(line)
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)
    
            elif param.find("lowercase")>-1:
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=lower(line)
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)

            elif param.find("mixed")>-1:
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=mixed(line)
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)
                    
            elif param.find("digits")>-1:
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=digits(line)
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)

            elif param.find("digit_avg_length")>-1:
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=dig_avg_len(line)
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)


            elif param.find("@")>-1 or param.find(".")>-1 or param.find("!")>-1 or param.find("?")>-1 or param.find(";")>-1:
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=special(unicode(line),unicode(param.strip()))
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)

            else:
                words=param.split()
                cur.execute('''SELECT spam_value,non_spam_value,weight from sms_spam WHERE id=?''',(p_id,))
                res=cur.fetchone()
                val=one(unicode(line),unicode(words[0].strip()))
                sp_val=res[0]
                ns_val=res[1]
                w=res[2]
                if abs(val-sp_val)>abs(val-ns_val):
                    total=total+w*(1)
                else:
                    total=total+w*(-1)


        if total>0:
            n_spam=n_spam+1
            
        else:
            spam=spam+1
            


    fh.close()
    cur.close()
    conn.close()
    print "Spams:",spam," Non Spam:",n_spam


def main():
    reload(sys)  
    sys.setdefaultencoding('utf8')
    check_spam_sms("spam_test.txt")
    check_spam_sms("ham_test.txt")

if __name__=="__main__":
    main()
