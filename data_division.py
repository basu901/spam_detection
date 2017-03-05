import sqlite3

#divide email data into spam and non-spam for training and testing
def segregate_email_data():
    data=open('spambase.data','r')
    smail_train=open('smail_train.txt','w')
    smail_test=open('smail_test.txt','w')
    nmail_train=open('nmail_train.txt','w')
    nmail_test=open('nmail_test.txt','w')

    smail_count=0
    nmail_count=0

    check=list()

    for line in data:
        check=line.split(",")
        if check[-1].strip()=='1':
            smail_count=smail_count+1
        else:
            nmail_count=nmail_count+1

    smail_test_count=smail_count/4
    nmail_test_count=nmail_count/4


    smail_train_count=0
    nmail_train_count=0

    print "nmail_count= ",nmail_count," smail_count= ",smail_count
    print "nmail_test= ",nmail_test_count," smail_test= ",smail_test_count

    data.seek(0)

    del check[:]

    count=0
    for line in data:
        count=count+1
        check=line.split(",")
        if check[-1].strip()=='1':
            if smail_test_count>0:
                smail_test.write(line)
                smail_test_count=smail_test_count-1
            else:
                smail_train.write(line)
                smail_train_count=smail_train_count+1
        else:
            if nmail_test_count>0:
                nmail_test.write(line)
                nmail_test_count=nmail_test_count-1
            else:
                nmail_train.write(line)
                nmail_train_count=nmail_train_count+1

    data.close()
    smail_train.close()
    smail_test.close()
    nmail_train.close()
    nmail_test.close()
    print count

    print "nmail_train_count= ",nmail_train_count,",","smail_train_count= ",smail_train_count


#separating parameters from provided file with headers
def make_complete_files():
    email_parameters=open('spambase_parameters.names','r')
    parameters_all=open('parameters.txt','w')

    for line in email_parameters:
        pos_end=line.find(':')
        param=line[10:pos_end]
        #print param
        if param.find('_')>=0:
            param=param[2:]
        parameters_all.write(param+'\n')

    email_parameters.close()
    parameters_all.close()  


#adding numbers for email database and rounding to 9 places
def copy_data(file_name):
    eh=open(file_name,'r')

    indices=dict()
    count=0
    for line in eh:
            count=count+1
            parts=line.split(",")
            del parts[-1]
            for index,val in enumerate(parts):
                try:
                    if float(val.strip())>0.0:
                        indices[index]=indices.get(index,0.0)+float(val)
                except:
                    pass

    count1=0

    cont=list()
    i=0
    for i in range(len(parts)):
        if i in indices.keys():
            cont.append(float(indices[i]))
        else:
            cont.append(0.0)
            count1=count1+1
    #print count1

    for i in range(len(cont)):
        cont[i]=round(cont[i]/count,9)

    return cont

#segregate data into training and test for ham and spam
def sms_files():

    fs=open('spam_messages.txt','r')
    fh=open('ham_messages.txt','r')

    fs_train=open('spam_train.txt','w')
    fh_train=open('ham_train.txt','w')

    fs_test=open('spam_test.txt','w')
    fh_test=open('ham_test.txt','w')

    count=0
    count1=0

    for line in fs:
        count=count+1

    for line in fh:
        count1=count1+1

    print count,'in spam ',count1,'in ham'

    count=count/4
    count1=count1/4

    fs.seek(0)
    fh.seek(0)

    count_train=0
    count1_train=0

    for line in fs:
        if count_train<count:
            fs_test.write(line)
            count_train=count_train+1
        else:
            fs_train.write(line)

    for line in fh:
        if count1_train<count1:
            fh_test.write(line)
            count1_train=count1_train+1
        else:
            fh_train.write(line)


    print count_train," train spam ",count1_train," train ham"


    
    

