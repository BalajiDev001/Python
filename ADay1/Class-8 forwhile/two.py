#iteration using list
eids=[101,102,103,104,105]
for eid in eids:
    # print(eid)
    print(eid,end='\t')  

#iteration using tuple
unames=('rahul','sonia','priyanka','modi')
for uname in unames:
    print(uname)    

#ieration using set

numbers={10,20,10,20}
for num in numbers:
    print(num)

#iteraton using str
enames="nandhini"    
for name in enames:
    # print(name) one by one 
    print(name,end='')   # side by side nandhini

#range
for value in range(5):
    print(value)    

#starting value **ending value **stepping value
for value in range(5,51,5):    
    print(value)    