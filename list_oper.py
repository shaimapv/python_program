list=[1,2,3,4,5]
print("original list is ",list)
print("first element is ",list[0])
print("last element is ",list[-1])
list[1]=25
print("updated list is ",list)
list.append(9)
print("after append list is ",list)
list.insert(2,30)
print("after inserting in to index 2 list is ",list)
list.extend([11,12])
print("after extend : ",list)
list.remove(4)
print("after removing 4 : ",list)
pop_item=list.pop()
print("popped item : ",pop_item)
print("after pop : ",list)
print("index of 3 is : ",list.index(3))
list.sort()
print("sorted list is : ",list)
list.reverse()
print("reversed list is : ",list)
print("length os list is : ",len(list))
list.clear()
print("after clearing : ",list)

"""
Output:
PS C:\training\6th task> python list_oper.py
original list is  [1, 2, 3, 4, 5]
first element is  1
last element is  5
updated list is  [1, 25, 3, 4, 5]
after append list is  [1, 25, 3, 4, 5, 9]
after inserting in to index 2 list is  [1, 25, 30, 3, 4, 5, 9]
after extend :  [1, 25, 30, 3, 4, 5, 9, 11, 12]
updated list is  [1, 25, 3, 4, 5]
after append list is  [1, 25, 3, 4, 5, 9]
after inserting in to index 2 list is  [1, 25, 30, 3, 4, 5, 9]
after extend :  [1, 25, 30, 3, 4, 5, 9, 11, 12]
after inserting in to index 2 list is  [1, 25, 30, 3, 4, 5, 9]
after extend :  [1, 25, 30, 3, 4, 5, 9, 11, 12]
after removing 4 :  [1, 25, 30, 3, 5, 9, 11, 12]
after extend :  [1, 25, 30, 3, 4, 5, 9, 11, 12]
after removing 4 :  [1, 25, 30, 3, 5, 9, 11, 12]
popped item :  12
after removing 4 :  [1, 25, 30, 3, 5, 9, 11, 12]
popped item :  12
popped item :  12
after pop :  [1, 25, 30, 3, 5, 9, 11]
index of 3 is :  3
after pop :  [1, 25, 30, 3, 5, 9, 11]
index of 3 is :  3
index of 3 is :  3
sorted list is :  [1, 3, 5, 9, 11, 25, 30]
reversed list is :  [30, 25, 11, 9, 5, 3, 1]
length os list is :  7
after clearing :  []"""
