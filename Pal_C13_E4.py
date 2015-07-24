######### Assignment 9 ##########
######### Navdeep Pal ###########
######### Date : 04/11/2015 #####

def list():
    inputList = eval(input(" Please enter a list of numbers you want a maximum for: "))
    print("The maximum number in the given list is: ", max(inputList))

list()


def max(inputList):
    if len(inputList) == 1: # Base condition
        return inputList[0]
    else:
        m = max(inputList[1:]) # Using recursion algorithm to find maximum
        return m if m > inputList[0] else inputList[0]