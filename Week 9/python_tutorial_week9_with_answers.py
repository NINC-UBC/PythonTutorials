# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:57:33 2016

previous file name was cycle0_week5.py

@author: jledue
"""

import numpy as np
import matplotlib.pyplot as plt

"""
As we have been learning about arrays, strings, loops, etc we've paused
a few times to check graphically that what we were doing made sense.  In
this tutorial we will spend more time exploring different types of plots
and figures in matplotlib.

Our goals are to introduce the basic plot commands (plot, bar) as well
as imshow which can be used to display 2D images.  We will
learn the basic commands for adding titles, lables, changing font size
and adding legends.  

Full documentation and examples on matplotlib are here:
http://matplotlib.org/index.html


2d line plots

First let's make some data for plotting. In this case a parabola.

1. Set up the x values as an ordered list.  Start the list at 0, use an
increment of 0.1 and end at 3.
"""

x=np.arange(.0,3,.1)

# 2. Square the x values and assign the result to a new variable called y1.

y1=np.power(x,2)

"""
When making plots you usually begin by creating a figure window.  Follow
that by the plotting command:
"""

plt.figure();
plt.plot(y1)

"""
3. Notice the x axis is the y1 index (0-30) replot again and make use of the
x values.
"""

plt.figure();
plt.plot(x,y1)

# This is the basic 2d plot.  We can add a title.  Highlight and run the
#next 3 lines together.
plt.figure();
plt.plot(x,y1)
plt.title('First plot example of a parabolic curve')

"""
% Notice the input to the title is a string.  So when we are working with
% our data, we can create titles that incorporate string variables (Such as
% the file name where the data came from).

% 4. Add the string 'x values' as an x axis label and the string 'y values'
% as a y axis label using the commands xlabel and ylabel
"""
plt.figure();
plt.plot(x,y1)
plt.title('First plot example of a parabolic curve')
plt.xlabel('x values')
plt.ylabel('y values')

"""
matplotlib's default fontsize is often too small.  People you share the plots
with will complain.

5. Re-do the plot and change the fontsize of the xlabel and ylabel to
match the title.  The commands are analogous.
"""

plt.figure();
plt.plot(x,y1)
plt.title('First plot example of a parabolic curve',fontsize=18)
plt.xlabel('x values',fontsize=18)
plt.ylabel('y values',fontsize=18)

# What about the axis tick labels? ie the numbers on the axes?

# try:
plt.figure();
plt.plot(x,y1)
plt.title('First plot example of a parabolic curve',fontsize=18)
plt.xlabel('x values',fontsize=18)
plt.ylabel('y values',fontsize=18)
plt.tick_params(labelsize=18)

"""
help(plt.tick_params)

will take you to a full list.  Fontsize is just one thing we can change.  

Another common one is to elimate the drawing of the axis on the top and
right hand sides, which makes the graph look boxed in.  This is a little more
complicated unfortunately.
"""

plt.figure();
#assign the axis to a variable so we manipluate them
ax = plt.subplot(111)
ax.plot(x, y1)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')


# or to add gridlines
ax.grid(1,which='major',axis='x')

"""
There are a lot of options, too many to go into each one, but the matplotlib
website mentioned at the beginning has a lot of examples.

Let's move to the situation where you want to plot more than one curve
together.

6. Create another variable called y2.  Assign it the values of x raised
to the 1.5 power instead of as we did for y1 above.
"""

y2=np.power(x,1.5)

"""
7. Let's begin by making a new figure window and plotting y1 vs x as we
did above.
"""

plt.figure();
plt.plot(x,y1)

# 8. plot y2 vs x is analogous way to y1.
plt.figure();
plt.plot(x,y1)
plt.plot(x,y2)

"""
Notice that by default matplotlib has colored the curves blue and green.

Let's say we wanted it the other way around.  We can add another argument
to the plot command to indicate the color.

Try:
"""


plt.figure();
plt.plot(x,y1,'g')
plt.plot(x,y2,'b')

"""
details are listed under help(plt.plot)

For example if we wanted a red line dashed and a blue one to have
circles marking the points.

Try:
"""

plt.figure();
plt.plot(x,y1,'--r')
plt.plot(x,y2,'ob')

# Now that we have two curves a legend also becomes important.
plt.figure();
plt.plot(x,y1,'--r',label='Power2')
plt.plot(x,y2,'ob',label='Power1.5')
plt.legend(loc='upper center', shadow=True, fontsize='x-large')

"""
% Let's move on to an example where we would like to represent the error
% bounds of multiple measurements.

% Let's add some random noise to our parabola
% Example: parabola with noise
"""
y1=np.power(x,2)+.5*np.random.randn(np.size(y1))

""" 9. plot it to see the effect of the noise."""

plt.figure();
plt.plot(x,y1)

"""
% 10.  Create an empty variable (filled with zeros) with space for 10 
% replicates of y1 called all_y1.  First store the value 10 in a variable
% called n_reps, so we can easily change it later.  Make all_y1 have 10
% columns and get the number of rows from the number of elements of y1.
"""
n_reps=10;
all_y1=np.zeros((np.size(y1),n_reps));

"""
11. Construct a for loop to store the result of 10 (n_reps) instances of our
parabola with noise.  These could be a signal we've measured in reponse
to 10 stimuli for example.

use i as your loop variable.  Start your loop variable at 1 and end at
n_reps (10).
"""

for i in np.arange(0,10):
    print(i)
    y1=np.power(x,2)+.5*np.random.randn(np.size(y1))
    all_y1[:,i]=y1
    
"""
Your loop can contain 2 commands, one like the Example: parabola with
noise above, which generates a parabola with noise and a second which
indexes all_y1 using the loop variable and stores the values in the 
correct places in the larger matrix.

Now try
"""

plt.figure();
plt.plot(all_y1)

"""
This plots all the columns so you can see the noise.

12.  Use the mean command to average all_y1 over the reps.  Store the
result in a variable called avg_y1.
"""

avg_y1=np.mean(all_y1,1)

"""
13 Use the std command to calculate the standard deviation at each x
value. Store the result in a variable called err_y1.
"""

err_y1=np.std(all_y1,1)

"""
Bonus: This is standard deviation, how would you get standard error of
the mean?

Note that you can do this directly with math, or google scipy.stats.sem

Now we can use fill between to represent the error bounds as a shaded region
"""

plt.figure();
plt.plot(x, avg_y1, 'k-')
plt.fill_between(x, avg_y1-err_y1, avg_y1+err_y1)

"""
Let's move on to Bar graphs.

14. Make two variables called b1, b2 & b3 assign one the values 10, 5, & 7.5.
"""

b1=10
b2=5
b3=7.5

"""
The matplotlib command for bar graphs is bar.  
"""
#define the x position of the groups
x=(1,2,3)
plt.figure();
plt.bar(x,(b1,b2,b3))

"""
It looks a bit rediculous with the bars so wide, so you can give bar a
third input to change this:
"""

plt.figure();
plt.bar(x,(b1,b2,b3),.3)

"""
Let's create another set of numbers representing the standard error of
the mean for each bar.
"""

err_b=(1, 1.5, .7)

#Another input to bar will handle the errors.
plt.figure();
plt.bar(x,(b1,b2,b3),.3,yerr=err_b)

"""
Lastly displaying images.

load in sample_image.jpg using imread, last time we used the scipy module to 
imread but matplotlib has one too.
"""

img=plt.imread("sample_image.jpg")
#recall you might need to use pwd and cd to navigate to the folder with the
#sample image or supply the full path.

#generate a figure window and then use imshow
plt.figure();
plt.imshow(img)

#or only the green channel

plt.figure()
plt.imshow(img[:,:,1])

# Bonus, How can the range of displayed grey values be changed?
plt.figure()
plt.imshow(img[:,:,1],vmin=25,vmax=175)

#Bonus 2, How can the colormap be changed?
#https://matplotlib.org/examples/color/colormaps_reference.html
plt.figure()
plt.imshow(img[:,:,1],cmap='hot')
