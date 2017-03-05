# -*- coding: UTF-8 -*-
#build trainig database for sms spam
import sqlite3
from decimal import *

def one(filename,w1):
    fh=open(filename,'r')
    total=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_words=0
    for line in fh:
        n=n+1
        words=line.split()
        del words[0]
        for word in words:
                if word.lower().find(w1)>-1:
                    count=count+1
                    count_total_words=count_total_words+1
                else:
                    count_total_words=count_total_words+1

        total=Decimal(count)/Decimal(count_total_words) + total
        count=0
        count_total_words=0

    fh.close()
    total=total/n
    return round(total,6)


def special(filename,s):
    fh=open(filename,'r')
    total=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_char=0
    for line in fh:
        n=n+1
        words=line.split()
        del words[0]
        for word in words:
            for ch in word:
                if ch==s:
                    count=count+1
                    count_total_char=count_total_char+1
                else:
                    count_total_char=count_total_char+1

        total=Decimal(count)/Decimal(count_total_char)+total
        count=0
        count_total_char=0

    fh.close()
    total=total/n
    return round(total,6)
                    

def digits(filename):
    fh=open(filename,'r')
    pro=Decimal(0)
    n=Decimal(0)
    count=0
    for line in fh:
        n=n+1
        words=line.split()
        del words[0]
        for word in words:
            for ch in word:
                try:
                    check=int(ch)
                    count=count+1
                except:
                    continue

        pro=Decimal(count) + pro
        count=0

    fh.close()
    pro=pro/n
    return round(pro,6)
            
def dig_avg_len(filename):
    fh=open(filename,'r')
    length_count=0
    avg_per_line=Decimal(0)
    count=0
    n=Decimal(0)
    av=Decimal(0)
    for line in fh:
        n=n+1
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
        
        av=av+avg_per_line
        length_count=0
        count=0
        
    av=av/n
    fh.close()
    return round(av,6)  

def lower(filename):
    fh=open(filename,'r')
    low=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_words=0
    for line in fh:
        n=n+1
        words=line.split()
        del words[0]
        for word in words:
                if word.islower():
                    count=count+1
                    count_total_words=count_total_words+1
                else:
                    count_total_words=count_total_words+1

        low=Decimal(count)/Decimal(count_total_words) + low
        count=0
        count_total_words=0

    fh.close()
    low=low/n
    return round(low,6)

def mixed(filename):
    fh=open(filename,'r')
    mix=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_words=0
    for line in fh:
        words=line.split()
        n=n+1
        del words[0]
        for word in words:
                if not word.islower() and not word.isupper():
                    count=count+1
                    count_total_words=count_total_words+1
                else:
                    count_total_words=count_total_words+1

        mix=Decimal(count)/Decimal(count_total_words) + mix
        count=0
        count_total_words=0
    mix=mix/n
    return round(mix,6)

def i_count(filename):
    fh=open(filename,"r")
    icount=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_word=0
    for line in fh:
        words=line.split()
        n=n+1
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

        icount=Decimal(count)/Decimal(count_total_word)+icount
        count=0
        count_total_word=0

    fh.close()
    icount=icount/n
    return round(icount,6)

def upper(filename):
    fh=open(filename,'r')
    up=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_words=0
    for line in fh:
        n=n+1
        words=line.split()
        del words[0]
        for word in words:
                if word.isupper():
                    count=count+1
                    count_total_words=count_total_words+1
                else:
                    count_total_words=count_total_words+1

        up=Decimal(count)/Decimal(count_total_words) + up
        count=0
        count_total_words=0

    fh.close()
    up=up/n
    return round(up,6)



def two_combined(filename,w1,w2):
    fh=open(filename,'r')
    total=Decimal(0)
    count=0
    n=Decimal(0)
    count_total_words=0
    count1=0
    count2=0
    for line in fh:
        n=n+1
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

            
        total=Decimal(count)/Decimal(count_total_words) + total
        count=0
        count_total_words=0
        count1=0
        count2=0

    fh.close()
    total=total/n
    return round(total,6)

def two_similar(filename,w1,w2):
    fh=open(filename,'r')
    total=Decimal(0)
    n=Decimal(0)
    count=0
    count_total_words=0
    for line in fh:
        n=n+1
        words=line.split()
        del words[0]
        for word in words:
                if word.lower().find(w1)>-1 or word.lower().find(w2)>-1:
                    count=count+1
                    count_total_words=count_total_words+1
                    
                else:
                    count_total_words=count_total_words+1

            
        total=Decimal(count)/Decimal(count_total_words) + total
        count=0
        count_total_words=0

    fh.close()
    total=total/n
    return round(total,6)



   
def main():

    conn=sqlite3.connect('spam.db')
    cur=conn.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS sms_spam(id INTEGER PRIMARY KEY,
        parameter TEXT NOT NULL,spam_value NUMBER,non_spam_value NUMBER,difference NUMBER,weight NUMBER)''')

    fhandle=open('sms_parameters','r')
    for line in fhandle:
        if line.find(",")>-1:
            words=line.split(",")
            sp_val=two_similar('spam_train.txt',words[0].strip(),words[1].strip())
            ns_val=two_similar('ham_train.txt',words[0].strip(),words[1].strip())
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        elif line.find("+")>-1:
            words=line.split("+")
            sp_val=two_combined('spam_train.txt',words[0].strip(),words[1].strip())
            ns_val=two_combined('ham_train.txt',words[0].strip(),words[1].strip())
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        elif line.find("i")>-1 and len(line)<3:
            sp_val=i_count('spam_train.txt')
            ns_val=i_count('ham_train.txt')
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))


        elif line.find("uppercase")>-1:
            sp_val=upper('spam_train.txt')
            ns_val=upper('ham_train.txt')
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        elif line.find("lowercase")>-1:
            sp_val=lower('spam_train.txt')
            ns_val=lower('ham_train.txt')
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        elif line.find("mixed")>-1:
            sp_val=mixed('spam_train.txt')
            ns_val=mixed('ham_train.txt')
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        elif line.find("digits")>-1:
            sp_val=digits('spam_train.txt')
            ns_val=digits('ham_train.txt')
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))


        elif line.find("digit_avg_length")>-1:
            sp_val=dig_avg_len('spam_train.txt')
            ns_val=dig_avg_len('ham_train.txt')
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        elif line.find("@")>-1 or line.find(".")>-1 or line.find("!")>-1 or line.find("?")>-1 or line.find(";")>-1:
            words=line.split()
            sp_val=special('spam_train.txt',words[0].strip())
            ns_val=special('ham_train.txt',words[0].strip())
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

        else:
            words=line.split()
            sp_val=one('spam_train.txt',words[0].strip())
            ns_val=one('ham_train.txt',words[0].strip())
            dif=abs(sp_val-ns_val)
            cur.execute('''INSERT INTO sms_spam(parameter,spam_value,non_spam_value,difference,weight) VALUES(?,?,?,?,1)''',(line,sp_val,ns_val,dif,))

    conn.commit()
    cur.close()


if __name__=='__main__':
    main()


    


    



