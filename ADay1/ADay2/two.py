a=10
b=[10,20,30]
c=[10,'rahul','raju']
d=[10,20,30]
 
print(id(a))
print(id(b))
print(id(b[0]))
print(id(c[0]))


print(a is b[0])
print(a is b)
print(b is c)
print(a==b[0])
print(b==d)