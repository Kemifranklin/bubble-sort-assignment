# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:47:17 2023

@author: kemi franklin
"""

"""
Name:
    buildildList
    Description: 
        this function will build a list containing some number of pseudo
        
"""
"""
NAME:
buildList3
DESCRIPTION:4
This function will build a List containing some number of pseudo-5
randomly generated integers. The number of integers generated is6
based on user input. The function returns the completed List7
structure to the caller.8
INPUT:9
none10
OUTPUT:11
A List containing some number of pseudo-randomly generated integers.12
"""
def buildList( ) -> list:
# Instantiate and empty List of ZERO length
    loadedList = [ ]
# How many elements should the List hold?
    elementCount = int(
    input( "How many elements should I create for your sort? " ) )
# Randomly generate integer values and load the List structure
    import random # For generating pseudo-random numbers

# Declare and initialize loop control variable
    counter = 0

# Set loop to add the required number of pseudo-random integers
    while ( counter < elementCount ):
# Retrieve pseudo-random integer; append to List
        loadedList.append( random.randint( 0, 101  ) )

# Increment the loop control
        counter += 1

# end iteration
# return the "loaded list" to the caller
    return loadedList
# end function buildList

#define a bubble sort list  
def bubblesort(buildList):
    sortedList=buildList[:]
#setting build list to sorted list 
    
    lenList = len(sortedList)
#lenth of lefgt set to sortedlist
    #enhanced for loop to set the range of list
    for listIndex in range(lenList): 
        for item in range(0,lenList-listIndex-1):#definning the range of the list with parameters .
            if sortedList[item] > sortedList[item+1]: #making the list sort from the smallest number to biggest numbe
                temp = sortedList[item]
                sortedList[item]= sortedList[item+1]
                sortedList[item+1]=temp
                
    return(sortedList)
#end bubblesort

def main():#defining main function
    
    unsortedList = buildList()
    print("Unsorted list:")#printing unsorted list
    print(unsortedList) #calling function
    sortedList = bubblesort(unsortedList)
    print("Sorted list :  ")#printing sorted list
    print(sortedList)#calling sorted function
        
    
main()
#calling main 
#end function

                
