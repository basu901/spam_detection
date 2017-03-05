#program to break the dataset into spam and ham
fh=open('SMSSpamCollection','r')
fw=open('spam_messages.txt','w')
f_ns=open("ham_messages.txt","w")
count=0
count_all=0
for line in fh:
        count_all=count_all+1
	if line.startswith('spam'):
                count=count+1
		fw.write(line)
	else:
                f_ns.write(line)
                
print "spam=",count,",","all=",count_all
fw.close()
fh.close()
