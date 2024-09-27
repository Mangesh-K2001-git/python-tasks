#Ex1.We have to create list of "string" having "A" as prefix from another list a = []

a = ["apple","Ant","Paper","Table","Chairs","Airpods","Atul","appu ghar"]

b = [words for words in a if words.startswith("A")]
print(b)

#Ex2.we have list of pallandrom from given list
a = ["1234","456","1221","454","997899","2013","191"]
b = [x for x in a if x==x[::-1]]
print(b)

#Ex3.we have list all number occured in given list
s = "Today at 9:30 we have our python lecture for 1/2 hours"
b = [int(num )for num in s if  num.isdigit()]
b.sort()
print(b)
