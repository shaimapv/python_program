employee={"name":"raj","age":25,"salary":25000,"gender":"male"}
print("original dictionary : ",employee)

print("\n---accessing values---")
print("name is : ",employee["name"])
print("age is : ",employee.get("age"))
print("salary is : ",employee.get("salary"))
print("city is : ",employee.get("city","unknown"))

print("\n---updating dictionary---")
employee["city"]="mumbai"
print("after updating : ",employee)

print("\n---deleting dictionary---")
del employee["gender"]
print("after deleting gender : ",employee)
popped_item=employee.pop("age")
print("deleted item is : ",popped_item)
print("after pop operation : ",employee)
last_item=employee.popitem()
print("popped item is : ",last_item)
print("after deleting ditionary is : ",employee)

employee.update({"name":"raj","age":5,"salary":25000})
print("length of the dictionary is : ",len(employee))

print("only keys : ",employee.keys())
print("only values : ",employee.values())

print("\n--copying a dictionary--")
copy_dict=employee.copy()
print("copy : ",copy_dict)

print("\n---merging dictionary---")
dict2={"city":"mumbai","Country":"india"}
employee.update(dict2)
print("after merge : ",employee)


print("\n--clearing dictionary--")
employee.clear()
print("after clear : ",employee)

"""Output:
PS C:\training\6th task> python dic_oper.py
original dictionary :  {'name': 'raj', 'age': 25, 'salary': 25000, 'gender': 'male'}

---accessing values---
name is :  raj
age is :  25
salary is :  25000
city is :  unknown

---updating dictionary---
after updating :  {'name': 'raj', 'age': 25, 'salary': 25000, 'gender': 'male', 'city': 'mumbai'}

---deleting dictionary---
after deleting gender :  {'name': 'raj', 'age': 25, 'salary': 25000, 'city': 'mumbai'}
deleted item is :  25
after pop operation :  {'name': 'raj', 'salary': 25000, 'city': 'mumbai'}
popped item is :  ('city', 'mumbai')
after deleting ditionary is :  {'name': 'raj', 'salary': 25000}
length of the dictionary is :  3
only keys :  dict_keys(['name', 'salary', 'age'])
only values :  dict_values(['raj', 25000, 5])

--copying a dictionary--
copy :  {'name': 'raj', 'salary': 25000, 'age': 5}

---merging dictionary---
after merge :  {'name': 'raj', 'salary': 25000, 'age': 5, 'city': 'mumbai', 'Country': 'india'}

--clearing dictionary--
after clear :  {}
"""