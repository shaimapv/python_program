set={1,2,3,4,5}
print("original set : ",set)

print("\nadd operation: ")
set.add(6)
print("after add : ",set)

print("\nupdate operation: ")
set.update([7,8])
print("after update : ",set)

print("\nremove operation:")
set.remove(2)
print("after remove : ",set)

print("\ndiscard operation: ")
set.discard(3)
print("after discard : ",set)

print("\nset operations: ")

set2={11,12,13}
print("second set : ",set2)

print("\nunion : ",set.union(set2))
print("\nintersection : ",set.intersection(set2))
print("\nset difference : ",set.difference(set2))
print("\nsymmetric difference : ",set.symmetric_difference(set2))

print("\nsubset and superset : ")
smallset={7,8}
print("is smallset a subset of set : ",smallset.issubset(set))
print("is set a superset of smallset : ",set.issuperset(smallset))

print("\ncopy operation : ")
copyset=set.copy()
print("copy : ",copyset)

print("\nclear operation : ")
set.clear()
print("after clear : ",set)

"""Output:
PS C:\training\6th task> python set_oper.py
original set :  {1, 2, 3, 4, 5}

add operation:
after add :  {1, 2, 3, 4, 5, 6}

update operation:
after update :  {1, 2, 3, 4, 5, 6, 7, 8}

remove operation:
after remove :  {1, 3, 4, 5, 6, 7, 8}

discard operation:
after discard :  {1, 4, 5, 6, 7, 8}

set operations:
second set :  {11, 12, 13}

union :  {1, 4, 5, 6, 7, 8, 11, 12, 13}

intersection :  set()

set difference :  {1, 4, 5, 6, 7, 8}

symmetric difference :  {1, 4, 5, 6, 7, 8, 11, 12, 13}

subset and superset :
is smallset a subset of set :  True
is set a superset of smallset :  True

copy operation :
copy :  {1, 4, 5, 6, 7, 8}

clear operation :
after clear :  set()"""
