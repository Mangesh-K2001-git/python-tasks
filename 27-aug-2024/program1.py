#dict:

#EX1.
flist={
    "a":"apple",
    "b":"banana",
    "c":"cat",
    "d":"dog",
    "e":"elephant",

}

print(type(flist))
print(flist)



print(flist["a"])
print(flist["b"])
print(flist["c"])
print("by using for loop:")
for key in flist:
    print(key,":",flist[key])

#EX2
'''mydict={
"name":"John",
"age":30,
"city":"New York",
}
print(mydict)
mydict.update({
    "name":"Jane",
    "age":25
})
print(mydict)'''


'''#EX4.
mydict={"name":"John","age":30,"city":"New York"}
print("original  dict: ",mydict)

print(mydict["name"])
mydict["name"]="mona"
print("after changing john to mona",mydict)'''

'''#ex5.
mydict={"name":"John","age":30,"city":"New York"}
print(mydict)

del mydict["city"]
print(mydict)'''

'''#EX5;
mydict={"name":"John","age":30,"city":"New York"}
print(mydict)
dic_length=len(mydict)
print(dic_length)'''




