#LIST data type overview

#a list of numbers
num = [9,6,7,1,5,3]
print (num)
#a list of strings
names = ["deepanshu","raghav","ian"]
print (names)
#a list of numbers and lists
list = [8,7,1,3,"raghav",43,"ian"]
print (list)
#to print first index of num list
print (num[1])
#to print first from last element in num list
print (num[-1])
#to print integers after 2nd index
print (num[2:])
#to print numbers from first to third index
print (num[1:3])
#to print both the num and name list
list1 = [num ,names]
print (list1)
#these are some functions on list
num.append(2)
print (num)
num.insert(2 ,15)
print (num)
#num.clear()
num.remove(15)
print (num)
num.pop(1)
print(num)
#num.pop()
num.reverse()
print (num)
#to calculate the sum of the list
c = sum(num)
print (c)
#to sort the list
num.sort()
print (num)
