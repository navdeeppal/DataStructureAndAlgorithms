######### Assignment 4 ##########
######### Navdeep Pal ###########
######### Date : 02/08/2015 #####
######### Chapter 7, Program exercise 12

################ Second Method ###############
#  This program accepts a date in the form month/day/year and outputs whether or not the date is valid.
import re

inDate = input("Please enter date in the format MM/DD/YYYY:")
parsingDate = re.match(r'(\d+)\/(\d+)\/(\d+)',inDate)
storingDate = parsingDate.groups()
inMonth = int(storingDate[0])
inDay = int(storingDate[1])
inYear = int(storingDate[2])
error = "This is an invalid date. Please recheck the date and enter again"

if (inDay <1 or inDay >31) or (inYear <1 or inYear >9999) or (inMonth < 1 or inMonth > 12):
    print(error)
    raise SystemExit(0)
    

if inMonth in [4,6,9,11]:
    if inDay == 31:
        print(error)
        raise SystemExit(0)
if inMonth == 2:
    if inYear%4 !=0:
        if inDay > 28:
            print(error)
            raise SystemExit(0)
    else:
        if inYear%4 ==0: #Leap Year
            if inDay >29:
                print(error)   
                raise SystemExit(0)           
                
print("Congratulations ,", inMonth,"/",inDay,"/",inYear," is a valid date! ", sep="")