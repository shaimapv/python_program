list= [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]
list.sort(key=lambda x:x[1])
print(list)

"""
Output:
PS C:\training\7th task> python lamda.py
[('Bob', 72), ('David', 85), ('Alice', 88), ('Charlie', 95)]
"""