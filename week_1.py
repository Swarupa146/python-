# -*- coding: utf-8 -*-
"""Week-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XAdvHTqRLfhMhbpThnwodm6ICsjP5F-3
"""

#A) Create a list and perform the following methods:
#1) insert() 2) remove() 3) append() 4) len() 5) pop() 6) clear()
a=[1,3,5,6,7,[3,4,5],"hello"]
print(a)
a.insert(3,20)
print(a)
a.remove(7)
print(a)
a.append("hi")
print(a)
len(a)
print(a)
a.pop()
print(a)
a.pop(6)
print(a)
a.clear()
print(a)
a=[1,3,5,6,7,[3,4,5],'hello']
del(a[2]) 
a
a=[1,3,5,6,7,9,'hello']
b=['python',2,4,8,10]
a.extend(b) #append to a sequence to a list
print(a)
a=[0,2,4,8,55,68,99]
a.reverse()
a
a=[55,44,99,66,11,23,78]
a.sort()
a
print(a, type(a))

#B) Create a dictionary and apply the following methods
#1) Print the dictionary items 2) access items 3) use get() 4)change values 5) use len()
x={"1":"Mango","2":"Kiwi",'3':"Jackfruit","4":'Cherry'}
y={1:10,2:25,3:63,4:75}
x=dict([('1','Mango'),('2','Kiwi'),('3','Cherry'),('4','Jackfruit')])
x
print(x)   #printing all elements present in the x and y
print(y)
print(x.keys())
print(x.values())
print(x.items())  #accessing items
z=x.get("Kiwi")  #using get() function
print(z)
dict1={'11':'Mango','24':'Kiwi','30':'Jackfruit','45':'Cherry'}
x['Cherry']=40  #changing values of a specific item
print(x) 
print(len(x))  #length of the elements  
print(len(y))
new=x.copy()  #copying elements
print('original:',x)
print('copy:',new)
x["Kiwi"]=25
print(x)
del(y[4])  #deleting particular item
y
print(dict1.pop("30"))
dict1
print(x, type(x))
y.clear()  #clearing all items present in y
print(y)

#C) Create a tuple and perform the following methods
#1) Add items 2) len() 3) check for item in tuple  4)Access items
x=()
x=(1,2,3,4,5)
x=1,2,3,4,5
x=2,
print(x, type(x))
list1=[2,4,6,8]
x=tuple(list1)
print(x, type(x))
x=x+(6,7,8,9)  #adding an items to an existing items
print(x)
print(len(x))  #length of the items
print(any(x))            #checking an item in tuple
x=['a','b','c','d']   #accessing an items
print(x[2:])
print(x[0])
y=(1,22,55,7,30,45,9,26,1,52,1,8)
y.count(1)     #returns no.of occurences of a values
y.index(55)    
x.clear()
x
del y
y

#set operations :
x=set()
x
list1={1,2,5,4,8}
x=set(list1)
print(x)
y={"Hello","Python"}
y.add("Programming")
print(y)