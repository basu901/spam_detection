#Spam Analysis
This is an experiment to analyze the specific features present in spam emails as well as spam sms'.The data for these experiments has been gathered from the following two links:

email:
https://archive.ics.uci.edu/ml/datasets/Spambase

sms:
http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/

All the data used for training,testing and building the databases has been collected from the above two links.
The email spam categorization algorithm is the basis on which the algorithm for sms spam categorization,has been built.

A screenshot of the chart showing the spam and non spam values for emails, for each parameter:

<br>
<img src="https://github.com/basu901/spam_detection/blob/master/chart.PNG"/>
<br>

A GUI is also available to categorize a sms as spam or ham(non spam):

<br>
<img src="https://github.com/basu901/spam_detection/blob/master/gui.PNG"/>
<br>

Please go through the READ_ME.txt for a detailed explanation.

Conclusion:
The approach used in identifying spam sms' was, to recognize the parameters which are characteristic of sms spams.They do tend to have a general nature whereas ham sms' have too large a variation to draw a circumference. It is interesting to note the prevalence of digits in spam sms'. It shows us how human actions in terms of investment, is dependent on the presence of facts. The factual data, provided in the form of digits, is one of the primary mechanisms used to lure people into transactions which are generally faulty.
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

Please do point out any mistakes regarding this experiment and I hope you had fun with the experiment as much as I did! Open to queries and suggestions!

