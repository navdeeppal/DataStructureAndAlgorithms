# Assignment 2: Data Structure and Algorithms
# Navdeep Pal
# Chapter 2 Programming Exercise 8
# Coverting Temperatures from Fahrenheit to Celsius

def tempFahrCel(): #Defining function 
    fahrenheit = eval(input("Please enter temperature in Fahrenheit: ")) # Taking user input and assigning to variable
    celsius = (fahrenheit-32) * 5/9 # Using formula for conversion
    print("Temperature in Celsius is: ", celsius, " degree C") # Printing output 
tempFahrCel() # Invoking function

    
    