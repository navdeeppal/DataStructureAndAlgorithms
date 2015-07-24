import string

s1= [2,1,4,3]
s2 = ['c', 'a', 'b']

print("a", s1+s2)
print("b", 3 * s1 + 2 * s2)
print("c", s1[1])
print("d", s1[1:3])
#print( s1 + s2[-1])


#a= s1.sort()
#print(s1)
#print(s1.remove(2))
#print(s1)
#print(s1.sort())
#print(s1)
#print(s1.append([s2.pop(2)]))
#print(s1)
#s2.pop(s1.pop(2))
#print(s2)
print(s2.insert(s1[0], 'd'))
print(s2)