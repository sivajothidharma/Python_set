#Empty set #set1=set()
#List May contain duplicates
#Set is ordered
#List and Tuples are unordered. It prints the value as it is
#The duplicate values are deleted in Set
#It doesn't have the indexing feature
#print("The Set values is ",set1)
#print(type(set1))
#Set is mutable
#is it possible to make it immutable?
#Yes, it's possible. Run frozenset function it will make it immutable

set2= {10,12, 9, 50}
list2=[10,12, 9, 50]
tuple2=(10,12, 9, 50)
print("The Set values is ",set2) #o/p: The Set values is  {9, 10, 12, 50}
print("The list values is ",list2) #O/P: The list values is  [10, 12, 9, 50]
print("The Tuple values is ",tuple2) #O/P: The Tuple values is  (10, 12, 9, 50)
print(type(set2))
set1=set(list2)
print("The list to set Conversition value is: ",set1)
#o/p" The list to set value is:  {9, 10, 12, 50}
str1='sivajothi'
print("String value: ", str1)
set2=set(str1) #Covert the string into set value
print("The string to set Conversition value is: ",set2)
#O/P: The string to set Conversition value is:  {'h', 'j', 'i', 's', 'v', 'o', 't', 'a'}
print("The type of string is :",type(set2))

from re import search

set1={10,20,23,12,10,12,15,50,100}
#Count
#Set doesn't have the count feature
print("The Total no of unike elements of Set is: ",len(set1))
#maximum
highest=max(set1)
print("The highest no of unike elements of Set is: ",highest)
#Lowest
lowest=min(set1)
print("The lowest no of unike elements of Set is: ",lowest)
#sorting
sort=sorted(set1)
print("The Sorted no of unike elements of Set is: ",sort)
#Set doens't allow to search the elements by index value
#print(set1[0]) - this function not allowed
#Searching

search=int(input("Enter the number to search for: "))
if search in set1:
    print("The entered no found in the set: ",search)
else:
    print("The entered no not found in the sets: ",search)

#Adding an element
set1.add(14)
print("Adding the value in the set is: ",set1)
set1.remove(14)
print("Removed the added value in the set: ",set1)
#Adding multiple values:
set1.update([11,17,7,5])
print("Updating the value in the set is: ",set1)
#Remove an element from the last
set1.pop()
print("Removing the value in the set is: ",set1)
#Remove the specific elements by value
set1.remove(17)
print("Removing the value in the set is: ",set1)
#Copy of the set
set2=set1.copy()
print("The new value of set2 is: ",set2)
#Mathematical functions:
set3={3,4,12,32,234,1,2,3,4,7,34}
print("The new value of set3 is: ",set3)
set4=set2.copy()
print("The new value of set4 is: ",set4)
#Union of sets
set5=set3.union(set4)
print("The new union value of set5 is: ",set5)
#Intersection- the Data of set1 not present in the data of set2
set6=set3.intersection(set4)
print("The new intersection set is: ",set6)
#difference of sets"
set7=set3.difference(set4)
print("The new difference value of set7 is: ",set7)
set8=set3.symmetric_difference(set4)
print("The new symmetric difference of set8 is: ",set8)
if set5.issubset(set4):
    print("The new symmetric difference of set8 is: ",set8)
fs=frozenset(set3)
print("The new frozenset of set3 is: ",fs)