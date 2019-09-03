# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:33:33 2016

@author: jledue

Note: file orginally named: cycle0_week5_MLw3.py, based on matlab tutorial week3.

"""

#Comment on the comments, notice the two different types of comments in python.
#If a line begins with a # it is ignored.

#Blocks of text can be isolated (see above) by """ & """

#Getting tired of all that typing to excute numpy and matplotlib
#commands?  Me too.  Software Carpentry avoids this shorthand but most examples you will
#find take the following shortcut to reduce typing and make code more readable.
import numpy as np
import matplotlib.pyplot as plt
#By importing the module as plt a matlabplot.pyplot.blah command becomes 
#simply plt.blah and likewise for numpy

# Numpy arrays are key as we will use them to store most types of
# data.  For example an image can be represented as a 2d array and a time
# course of a signal can be represeted by a 1d array.

# Our goals are to review and practice basic indexing commands
# and introduce and practice accessing subsets of array elements that satisfy a
# condition.  This is called logical indexing.

# Accompanying this file is a .npy file called dat.npy.  These files typically 
# store variables.  I generated the file with these lines of code.

dat=np.random.randn(100,100)
np.save('dat.npy',dat)

# and then deleted it from memory with
#del dat

#The variable contained in the file is a 100x100 array.  The purpose of the file
#is simply to ensure that everyone has the same data and will get the same results
#below.

#To load in the data in the file we need to do a couple of things:
#In the python window below, type pwd.

#This is shorthand for "print working directory".  If the result is not the folder that 
#contains your dat.npy file you will need to follow the pwd command by cd <my_folder>.
#The cd stands for change directory.  You can use sequential commands to move to the right
#folder.  For example on my laptop, I used:

cd Desktop
#followed by
cd python-novice-inflammation-data

#Note that you can use cd .. to move back a folder if needed.

#Once you get to the right place, try:
np.load('dat.npy')

#python uses numpy to read in the data in the file and a snippet of the data is displayed
# so you can take a look.

#However, note that in the environment tab on the right hand side, nothing is there.
#This is because we have not assigned the data we have read in to a variable.
#Try:

dat=np.load('dat.npy')

# Basic indexing (also referred to as slicing by software carpentry) allows you to pull out 
#subsets of the elements of a larger array.  To use basic indexing we specify the elements 
#we want with numbers or lists of numbers

# Let's use basic indexing to get the values of some elements of this weeks
# 2d matrix dat:

#1. What's the value of the element in the first row and first column?



# 2. What are the values in the 50th row, columns 1:10? Hint: Rows preceed
# columns when indexing.



# Let's use basic indexing in combination with some other syntax:

# 3. What's the sum of every other element in row 51, starting with the
# first? Hint: use the syntax start:finish:increment to generate an ordered
# list with an increment other than 1.  Also help(np.sum)



# 4.Starting with the 2nd?



#Does it make sense? Compare the sum of the above 2 sums with the sum of all the elements
#to double check that no elements have been missed.

# 5.  What's the sum of the upper right quadrant?

# For help try:

help(np.sum)

# 6.  Extract the 4th column.  Store it a variable called the_fourth.  Plot
# it using the following commands.


plt.figure()
plt.plot(the_fourth)
plt.title('Jeff"s Random Numbers')
plt.xlabel('index')
plt.ylabel('the random value')

# 7. Say we are interested in which value in the_fourth column of dat is
# the smallest.  Write a command which uses the built in numpy function
# amin as well as argmin to find both the value and its index.  
# index the_fourth such that this value
# alone is exluded from the matrix.

#These may be useful

help(np.amin)
help(np.argmin)
help(np.delete)


# 8.  Repeat #7, but this time find the value closest to 1 and exclude it.

# Hint:  You may want to look at:

help(np.absolute)



# Ok, let's move on to logical indexing.

# Logical indexing is useful when we are interested in a subset of array
# elements that satisfy a condition.  For example if our 2d array
# represents an image then we can think of applying a threshold to the
# image at a certain intensity as an example of logical indexing.

# To set up conditions based on the relative sizes of the values of the
# array elements we need to make use of the relational operators.

# The basic relational operators are:
#  > greater than
#  >= greater than or equal to
#  < less than
#  <= less than or equal to
# != not equal
# == is equal to

# Note the equals sign is used for assignment of a value to variable when
# it appears once, =, and for comparison of values when it appears twice,
# ==.

# Let's isolate the first 10x10 elements of dat for some examples.  Assign
# the first 10x10 elements of dat to a variable called dat10.

dat10=dat[0:10,0:10]

# Say we are interested in the values which are greater than zero.

A=dat10>0

# The result is a 10x10 array, with an element corresponding to each in dat10.  If you look
#in the environment you should see that A is 10x10 aray.

#Try:
A.dtype

#This numpy method returns the type of the data stored in the elements of the numpy array.

# bool is short for boolean and it means that each element can be either True (1) or False (0) 
#depending on whether that element of dat satisfied the condition we were interested in.  

# For example element 0,0 of A is False

A[0,0]

# which indicated that dat10[0,0] is a negative value.  Let's check.

dat10[0,0]

# The value returned is -0.004 so it checks out.

# We can use A as an index for dat10 and retireve only the positive values.

dat10[A]

#It is important to note that if you are not interested in the values of A
#it is not required to store them in a named variable. The command:

dat10[dat10>0]

#accomplishes the same task as we performed above in a single line.

# 9. Use the <= operator to create a variable called B which is analogous
# to A and stores Ture where the value in dat10 is <= 0 and False where it is
# not.


# Use B to index dat10 and print the values to the screen.  Use indexing to 
# check your work as we did for A.  If an element of B is True that should mean
#the corresponding element of dat10 is 0 or less.
 

# Bonus: Use the built-in numpy function size to find the number of
# elements in dat10(A) & the number of elements in dat10(B).  What is the sum?  
# Does it make sense?  If not what should it be?


# Bonus2:  If you are given A, write a command to generate B which does not
# make use of the orignal values in dat10.  Store the result in C.  

#Hint, the numpy function astype converts the elements of an array from one type to another
# ie, 1,0 -> True, False
# The numpy command array_equal compares to matrices to see if their sizes and elements
# are equal.  Use this to compare B & C to check your work.



# Another related command useful for logical indexing is called where.

# For exmaple, say we were interested in those points in the_fourth which
# were greater than or equal to 1.  We could write:

ind=np.where(the_fourth>1);

# you will see ind in the environment to the right.  It is a list of those indices which 
# satisfy the condition.  This can be used to isolate the values in the_fourth:

# Evaluate:

the_fourth[ind]


# 10.  Write a command that locates the same values as we found with np.where but uses 
# logical indexing as we first introduced it.
