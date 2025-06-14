tuple=(1,2,3,4)
print("actual tuple : ",tuple)
print("first element : ",tuple[0])
print("last element : ",tuple[-1])
tuple2=(5,6)
print("after concatenation : ",tuple+tuple2)
print("reverse of a tuple : ",tuple[::-1])
print("length of a tuple : ",len(tuple))
print("index of 4 is : ",tuple.index(4))
print("count of 1 is : ",tuple.count(1))
print("maximum element is : ",max(tuple))
print("minimum element is : ",min(tuple))
sorted(tuple)
print("after sort : ",tuple)
print(all(tuple))
print(any(tuple))

"""
Output:
PS C:\training\6th task> python tuple_oper.py
actual tuple :  (1, 2, 3, 4)
first element :  1
last element :  4
after concatenation :  (1, 2, 3, 4, 5, 6)
reverse of a tuple :  (4, 3, 2, 1)
length of a tuple :  4
index of 4 is :  3
count of 1 is :  1
maximum element is :  4
minimum element is :  1
after sort :  (1, 2, 3, 4)
True
True
"""