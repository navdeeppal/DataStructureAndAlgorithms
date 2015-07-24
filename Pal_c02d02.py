# Assignment 2: Data Structure and algorithms
# Navdeep Pal 
#Program Chaos

# A program illustrating chaotic function 

def chaos(): #Defining a function "chaos"
    print("This program illustrates chaotic behavior") # Output, Just printing text
    x = eval(input("Enter a number between 0 and 1: ")) # Assignment, Asking input from user and assigning it to variable "x"
    for i in range(10): # Definitive Loop
        x = 3.9*x*(1-x) # Assignment statement
        print(x) # Output, also ends definitive loop
chaos() # Invoking function "Chaos"