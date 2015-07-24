######### Assignment 6 ##########
######### Navdeep Pal ###########
######### Date : 02/21/2015 #####
# Removes duplicate from a List
#inputList = list(input("Type a list of numbers or alphabets without any separator : "))



def removeDuplicates(somelist):
    #remDup = [inputList[i] for i in range(len(inputList)) if not inputList[i] in inputList[:i]]
    remDup = []
    for num in somelist:
        if num not in remDup:
            remDup.append(num)
    print("List you entered is: ", somelist)
    print("The list after removing duplicates", (remDup))
    
removeDuplicates(['a','f','e', 'a', 'f', 'g', 'h',1,3,5,3,2,5,6,7,4,3])