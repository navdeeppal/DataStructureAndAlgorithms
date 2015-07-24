######### Assignment 6 ##########
######### Navdeep Pal ###########
######### Date : 02/20/2015 #####

s1 = "spam"
s2 = "ni!"

# Part A

print("a", "The Knights who say, " + s2)
print("b", 3 * s1 + 2 * s2)
print("c", s1[1], "d", s1[1:3], "e", s1[2] + s2[:2], "f", s1 + s2[-1], "g", s1.upper(), "h", s2.upper().ljust(4) *3)

#Discussion 2

print(s2[:2].upper())
print(s2 + s1 + s2)
print(3* (s1.capitalize().ljust(5)+ s2.capitalize().ljust(5))) 
print(s1)
print([s1[:2], s1[3]])
print(s1[0:2]+s1[3])

for ch in "aardvark":
    print(ch)
    
for w in "Now is the winters of our discontent...".split():
    print(w)
    
for w in "Mississippi".split("i"):
    print(w, end = " ")

msg = ""
for s in "secret".split("e"):
    msg = msg + s
print(msg)

msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch)+1)
print(msg)


# Discussion 4

print("Looks like {1} and {0} for breakfast".format("eggs", "spam"))

print("There is {0} {1} {2} {3}".format(1,"spam", 4 , "you"))

print("Hello {0}".format("Susan", "Computewell"))

print("{0:0.2f} {0:0.2f}".format(2.3, 2.3468))

print("{0:13.5f} {0:3.5f}".format(2.3, 2.3468))

print("Time left {0:02}:{1:05.2f}".format(1,37.374))

#print({1:3}.format("14"))

# Chapter 11 Discussion

# Discussion 1



 



