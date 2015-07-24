######### Assignment 9 ##########
######### Navdeep Pal ###########
######### Date : 04/11/2015 #####


def sent():
    inputSen = input("Please enter a string you want to evaluate:")
    inputSen = inputSen.lower()
    palind(inputSen)
    
def palind(inputSen):
    if len(inputSen) == 1 or len(inputSen) == 0:
        print("The given string is a Palindrome")
        return
    if not inputSen[0].isalpha():
        return(palind(inputSen[1:]))
    if not inputSen[-1].isalpha():
        return(palind(inputSen[:-1]))        
    if inputSen[0] == inputSen[-1] and len(inputSen) > 1:
        return palind(inputSen[1:-1])
    
    if inputSen[0]!= inputSen[-1]:
        print("The given string is not a Palindrome")
    
sent()