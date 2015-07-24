######### Assignment 5 ##########
######### Navdeep Pal ###########
######### Date : 02/15/2015 #####
# sumnums(numbers) returns the sum of all arguments (eg, sumnums(2, 3, 5) returns 10, sumnums(2,3,5,10) returns 20).

def sumnums(*numbers):
    sumList = 0
    for i in numbers:
        sumList = i+ sumList        
    print("The sum of numbers in the list is:", sumList)

sumnums(2,3,5,18,20,-20,90,-80)