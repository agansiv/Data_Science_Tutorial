# Learning all the variables /numbers /lists/tuples/dictionaries


var = "String"  # Variables ,strings are immutable
print("Var  is of string type ", type(var))
# print string on multiples line and use + sign to concatenate
print(''' I am just  a learning and 
will learn the ''' + 'python')

num = 100
print("num  is of number  type ", type(num))

flo = 100.00
print("flo  is of number  type ", type(flo))

print("// is to get the real number of division like 3/4 is 0.75  and // returns 0 ", 3 // 4)

print("% gives the reminder of the division  like if we divide 5 by 4  reminder will be 1 ", 5 % 4)

# conversion from one data type to another like str(),int()

## Dealing with List
'''
    1. Lists are mutable , we can append ,remove and insert
    2. Can be accessed by using the indexes
    3. We can iterate the items in list using loops 
    4. we can concatenate the Lists
    
'''
li = [1, 2, "a", "b"]

print(li)
print(li[1])  # index starts with 0
print(len(li))  # returns the number of items in the list

li.append("second_place")  # append allways adds at the end
print(li)

li.insert(2, "third_place")
print(li)

n = 999
for items in li:
    if n == 999:
        print("Index | Values")
        n = 0
    print(" | ",n, " | ", items," | ")
    n += 1

print(li[0:3]) #  list can be accessed partially like starting [0:4] where its starts from 0 and 4 is excluded
print(li[3:])
'''
  [0:5]  0 to 4 are displayed
  [: 4]  starting from 0 as default when not mentioned to the  3 in this example
  [2:4]  starting from 2 to 3 
  [2:]   starting from 2 to till end 
'''
print(li)
lii = []
li.remove("b") # delete the value using value
print(li)
lii = li
li.append("b")
print(li)
li.remove(li[5]) # delete using the index
print(li)
#for loop
print("*"*40)
print("for loop started ")
for items in li:
    pass
    #print(items*2)
if 3 in li:
    print ("yes can find it ")
else:
    print("Sorry Cant find")


###### Dealing with Dictionries
'''
    1. Dictionaries are mutalble and unordered
    2. Can add values directly like dictt["d"]= 999
    3. Can delete the values like del dictt["a"]
    4. Can update the values in dictt
'''
dictt  = {"a":123,"b":456,"c":789}

print(dictt["a"])

dictt["d"]=999
print(dictt)
del dictt["a"]
print(dictt)
di =dictt
print(di)

for dd,cc in dictt.items():
    print(dd ," ",cc)


print("^"*40)

if "b" in dictt:
    print (dictt["b"])

print(dictt)
for key,val in dictt.items():
    #va =  "i am simple %("+key+")s"
    print("key is %s and value is %s" % (key,val))

for key,val in dictt.items():
    print("the key is %s" % key)


##### Multidimensional Listss
#mul_list = [[a , b],[c, d],[e, f],[g, h],[i, j]]
mul_list = [[1,2],["a","b"]]
number_sets = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(mul_list[0][1])
print(number_sets[2][3])
print(number_sets)
#print(number_sets[1].reverse())
bi =[1,2,3,4]
bi.reverse()
print("output is :",bi)
bi.sort()
print(bi)


### Dealing with tuples
'''
    1. Tuples are immutable
    
'''
tu = ('a',1,'c',2,)
print (tu)

for i in tu:
    print("the value is : %s" % i)


### Dealing with Modules

import math

#print(dir(math))

import sys

print(sys.path.append("c:\\Work"))
print(sys.path)


#### Dealing with JSON  files

book = {}

book["bob"] = {
    "name" : "Bob",
    'phone' : 123
}

book ["smith"] = {
    "name" : "smith",
    "phone" : 455
}

print("Hereeeee  ",book)
print("Doneeee",book["smith"])

import json
import pprint
s= json.dumps(book)
print(s)
pprint.pprint(json.loads(s))
#print(book[1])



