#data types
"""a=10
b=10.20
c="111"

print(type(a))
print(type(b))
print(type(c))
print(c)
"""
#int,float,str,bool,list,tuple,dict,set,range,None

#list
"""l=[1,2,3,4]
print(l)
print(type(l)) #list
l.append(5)
print(l)
print(l)
l.append(1)
print(l)
print(l)
l.append('abc')
print(l)

"""
#tuple
t=1,2,3,4
print(type(t))
t1=1,
print(type(t1))
t1=(100,111,121,'abc',111)
"""t1.append(121)
print(t1)
"""
print(t1)
print(t1[0])

t2=list(t1)
print(t2)
t2.pop()
print(t2)
t3=tuple(t2)
print(t3)


# set data type

s={9,2,3,4,'abc'}
print(s)
s.add(100)
print(s)
s.remove('abc')
print(s)
#A-B

s1={9,2,3,4,'abc'}
s2={9,111,3,222}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))#s1-s2
print(s2.difference(s1))#s2-s1




s3={100,200,200,400,900,800,500,900}
print(s3)




























