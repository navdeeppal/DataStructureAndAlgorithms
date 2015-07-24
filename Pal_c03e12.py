# Sum of the cubes of the first n natural numbers, where the value of n is provided by the user
# Assignment 3, Data Structure and Algorithms
# Navdeep Pal 


print("This program calculates sum of the cubes of the first n natural numbers, where the value of n is provided by the user \n")
inputNum = eval(input("Please enter a natural number: "))
type(inputNum)
cubeNum = (inputNum*(inputNum+1)/2)**2 
print("Sum of the cubes of the first", inputNum, "natural numbers is", cubeNum  )
