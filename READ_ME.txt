This is an experiment to analyze the specific features present in spam emails as well as spam sms'.The data for these experiments has been gathered from the following two links:

email:
https://archive.ics.uci.edu/ml/datasets/Spambase

sms:
http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/

All the data used for training,testing and building the databases has been collected from the above two links.
The email spam categorization algorithm is the basis on which the algorithm for sms spam categorization,has been built.

The file data_division.py is used to demonstrate how the data was segregated into testing and training.This program will result in an error unless the files are present with the same names as in the program.The data can be downloaded from the above links if you wish to run the program.

The two folders, email_spam_files and sms_spam_files contain data related to email spam and sms spam respectively.

NOTE : The database 'spam.db' is common to both email and sms spam and must be present in the same folder while running any of the programs.

email_spam_files:

1) email_chart_data.py is used to load the data for the email_train_data.js file.The email_train_data.html calls the data available in email_train_data.js to load and display the graph in a browser.The values in the graph denote the average occurrence of each parameter in spam emails as well as non spam emails.

2)email_test.py is used to test the percentage of spam and non spam mails detected.The program accesses the data in nmail_test.txt and smail_test.txt...nmail_test.txt contains all the non spam emails(which have been segregated previously from the source mentioned above) and smail_test.txt contains all the spam emails(also segregated).Hence,the efficiency of the algorithm depends on the percentage of non spam or spam(depending on the file) it detects,as we already know whether the emails being tested is spam or not.On running this program(remember to place the spam.db in the same folder),we will get the following output:

(smail_test.txt)
Total Number of emails= 453
Spam mails= 419  % Spam= 92.49
Non Spam mails= 34  %Non Spam= 7.51

(nmail_test.txt)
Total Number of emails= 697
Spam mails= 88  % Spam= 12.63
Non Spam mails= 609  %Non Spam= 87.37

Conclusion:
The algorithm used is fairly efficient and forms the basis of testing spams for sms.


sms_spam_files:
1)sms_segregate.py is a program demonstrating how the data was segregated.The sms spam data collection was divided into spam and ham after which 3/4 of each spam and ham was used for training.The remaining 1/4 of each was used for testing.The data sources are available from the links mentioned above.Running this program will result in an error as all the data that has been segregated and extracted has been used for building the database spam.db

2)sms_db_build.py shows how the database for sms_spam has been built.The file accessed in this program was used for building the database.All the data which was present in 'sms_parameters' has been used to populate the 'parameters' column in the 'sms_spam' table.'spam_train.txt' and 'ham_train.txt' contained 3/4 each of the spam and ham data used for training.

The above two programs are present for providing an insight of how the database for sms_spam was built.

3)test_sms_spam.py is used to test the algorithm for spam and ham detection.The files accessed are 'spam_test.txt'(all of which are spam sms') and 'ham_test.txt'(all of which are ham sms').The corresponding values obtained are:

Spams: 144  Non Spam: 42
Spams: 2  Non Spam: 1204

Hence we the algorithm is 77.42% effective in recognizing spam and 99.8% effective in recognizing ham or non spam.

4)sms_application.py is an interactive program to check whether an input sms is categorized as spam or not...test.py contains the helper functions accessed by this program.

Conclusion: The approach used in identifying spam sms' was, to recognize the parameters which are characteristic of sms spams.They do tend to have a general nature whereas ham sms' have too large a variation to draw a circumference. It is interesting to note the prevalence of digits in spam sms'. It shows us how human actions in terms of investment, is dependent on the presence of facts. The factual data, provided in the form of digits, is one of the primary mechanisms used to lure people into transactions which are generally faulty.
I checked a bunch of sms' the results of which are:

What's up? Are you free tonight? Give me a call at 9997886662!!=Spam
What's up? Are you free tonight? Call me.=Not Spam
Give me a call tonight.Wanna meet! Number:9875673921=Spam
Call me at :9875673921 Can't wait!!=Spam
My Number:9875673921=Not Spam
Ray:9875673921.Speak to him and ask him if the offer is available=Not Spam
Free Mobile Phones!! Hurry!! Offer valid ONLY till the end of THIS 28/4/2017.SUBSCRIBE 2 our website at www.mobile.com for more details=Spam
Free Mobile Phones!! Hurry!! Offer valid ONLY till the end of THIS month.SUBSCRIBE 2 our website at www.mobile.com for more details=Not Spam

What I could gather is, ham messages containing any personal information in the form of digits is prone to be categorized as spam. Though these types of sms' form a very minute set in the pool of ham sms', it is not only erroneous but also dangerous. One way around might be check the remaining text for 'spam-like' behaviour. Also, it is increasingly difficult to identify spams which are written in colloquial language,further aggravated by the absence of numbers.A completely new range of studies is probably required in this context of 'colloquial' spam!

Please do point out any mistakes reagrding this experiment and I hope you had fun with the experiment as much as I did! Open to queries and suggestions!


