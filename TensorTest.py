"""Tensorflow Stock Prediction Test written by Sakari Woods.
This uses a csv file of SP500 stock information to graph all prices,
then graphs a moving average to visually demonstrate where points-of-interest are located.
Once these are displayed, the SP500 price information is fed into a Tensorflow neural net
in order to locate trends or correlations in prices.
Finished:
Data importation and filtering
Plotting system
Currently working on:
Implementation into Tensorflow
Up next:
Coloring plotted lines as a heat-graph to show how content the AI is with it's decision.
"""

#Dependencies are imported here
import tensorflow
import pandas as pd
import matplotlib.pyplot as pt

#Import the stock data using pandas, a very useful library that can manipulate csv files.
data = pd.read_csv('sp500.csv')

#The first column of the csv has the dates. Because we only want price values, we can remove this from imported data.
#(we could keep this in order to factor in time-spans of when stocks increased, and how long were they deemed profitable, maybe later!).
#data = data.drop(['DATE'], 1)

#Set the dimensions of the data, think of this as we're setting the dimensions of a big box that holds our data.

#NEEDS EDIT HERE FOR EASIER EXPLANATION ON NUMPY DIMENSION ASSIGNMENT.
#Note: How the coordinates work in this data is as such: [5][3] would be the data in the csv file 5 rows down, 3 rows to the right.
n = data.shape[0]
p = data.shape[1]

#We take our stock data and turn it into a numpy array(this is what our plotter and Tensorflow will use).
data = data.values

#Set the window size to something manageable, put a label on it, and set the color of the line to blue. Note we chose data[0], that is our csv information for all SP500.
#(The csv offers other stock information, but we're just messing with SP500).
#We also set the limits of our viewing window so the lines aren't compressed or too stretched out, and we give the graph a nice title and legend, located on the upper right.
print(data[0])
pt.figure(figsize=(10,5))
pt.xlim(0,50)
pt.ylim(2340,2370)

#pt.plot(data[0],"-b", label="Prices")
vdat = []
for i in range(75):#Developer note to switch out vdat and iterative loop for faster results by passing in raw data of .csv file.
    vdat.append(data[i])
pt.plot(vdat,"-r",label="Price")
pt.title("Stock Prediction Test")
#This piece is a little weird, we create another array out of our SP500 data, an enumerate it inside a for loop while calculating the average of each value, and the value behind it.
#Basically, this gets the average, and makes an array of all average values for all SP500 data. Pretty neat!
#mylist = data[0]
mylist = vdat
N = 3
cumsum, moving_aves = [0], []
for i, x in enumerate(mylist, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        #can do stuff with moving_ave here
        moving_aves.append(moving_ave)

#Using the average data, we plot another line, this time named "Moving Average", and make it red.
pt.plot(moving_aves,"-b", label="Moving Average")
pt.legend(loc='upper right')
#Finally, we tell the program to render and draw everything on the screen.
#pt.show(data.all())
#pt.show()

#IN DEVELOPMENT: TENSORFLOW INTEGRATION FOR RECURRENT NEURAL NETWORK

#Evaluate derivatives
print("EVALUATING")
pchange = []
print(data[0])
print(data[1])
pchange.append(data[0]-data[1])
print("pchange is ",pchange[0])
print(data[2])
print(data[3])
pchange.append(data[1]-data[2])
print("pchange is ",pchange[1])
print("DONE")
a = 10
b=2365
area= (30 * 5)
colors = "g"
pt.scatter(a,b,s=area,c=colors,alpha=0.5)
#pt.plot(pchange,"-g", label="Derivative")
pt.show()

#Bookmark for additional development on structuring data into tensorflow.
