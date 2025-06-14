def add(n1,n2):
    print(n1+n2)

def subtract(n1,n2):
    print(n1-n2)

def multiply(n1,n2):
    print(n1*n2)

def divide(n1,n2):
    if n2==0:
        print("Syntax error")
    print(n1/n2)

def modulus(n1,n2):
    if n2==0:
        print("Syntax error")
    print(n1%n2)


num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
op=input("Enter operation to be performed (+,-,*,/,%) : ")
if op == "+":
    add(num1,num2)
elif op=="-":
    subtract(num1,num2)
elif op=="*":
    multiply(num1,num2)
elif op=="/":
    divide(num1,num2)
elif op=="%":
    modulus(num1,num2)
else:
    print("Syntax error")


"""Output:
PS C:\training\7th task> python calculator.py
Enter a number : 5
Enter a number : 6
Enter operation to be performed (+,-,*,/,%) : +
11
PS C:\training\7th task> python calculator.py
Enter a number : 6
Enter a number : 9
Enter operation to be performed (+,-,*,/,%) : -
-3
PS C:\training\7th task> python calculator.py
Enter a number : 4
Enter a number : 3
Enter operation to be performed (+,-,*,/,%) : *
12
PS C:\training\7th task> python calculator.py
Enter a number : 6
Enter a number : 3
Enter operation to be performed (+,-,*,/,%) : /
2.0
PS C:\training\7th task> python calculator.py
Enter a number : 6
Enter a number : 6
Enter operation to be performed (+,-,*,/,%) : %
0
PS C:\training\7th task> python calculator.py
Enter a number : 6
Enter a number : 9
Enter operation to be performed (+,-,*,/,%) : _
Syntax error
"""