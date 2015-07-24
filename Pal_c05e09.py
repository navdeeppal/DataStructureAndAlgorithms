# Writing a program that counts the number of words in a sentence entered by the user
# Assignment 3, Data Structure and Algorithms
# Navdeep Pal

print("This program counts the number of words in a sentence entered by the user")

sentence = input("Enter a sentence for that you want to count the words: ")

countWord = len(sentence.split()) # this code assumes that words are separated by space

print("Given line has", countWord, "words.")
