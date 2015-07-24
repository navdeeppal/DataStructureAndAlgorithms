######### Assignment 4 ##########
######### Navdeep Pal ###########
######### Date : 02/08/2015 #####
######### Chapter 7, Program exercise 12

################ First, Automated Method ###############
#  This program accepts a date in the form month/day/year and outputs whether or not the date is valid.

import time

inDate = input("Please enter date in the format MM/DD/YYYY:")

try:
    dateIn = time.strptime(inDate, "%m/%d/%Y") 
    print("Congratulations ,", dateIn.tm_mon,"/",dateIn.tm_mday,"/",dateIn.tm_year," is a valid date! ", sep="")
    
except ValueError:
    print("This is an invalid date. Please recheck the date and enter again")




