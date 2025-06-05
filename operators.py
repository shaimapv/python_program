def arithmetic():
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    print(f"num1 + num2 = {num1 + num2}")
    print(f"num1 - num2 = {num1 - num2}")
    print(f"num1 * num2 = {num1 * num2}")
    print(f"num1 / num2 = {num1 / num2}")
    print(f"num1 % num2 = {num1 % num2}")
    print(f"num1 // num2 = {num1 // num2}")
    print(f"num1 ** num2 = {num1 ** num2}")

def assignment():
    num1 = int(input("enter a number to perform assignment operations : "))
    print(f"num1 = {num1}")
    num1 += 2 ; print(f"num1 += 2 -> {num1}")
    num1 -= 3 ; print(f"num1 -= 3 -> {num1}")
    num1 *= 4 ; print(f"num1 *= 4 -> {num1}")
    num1 /= 2 ; print(f"num1 /= 2 -> {num1}")
    num1 %= 3 ; print(f"num1 %= 3 -> {num1}")
    num1 //= 2 ; print(f"num1 //= 2 -> {num1}")
    num1 **= 3 ; print(f"num1 **= 3 -> {num1}")
    
def comparison():
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    print(f"num1 == num2: {num1 == num2}")
    print(f"num1 != num2: {num1 != num2}")
    print(f"num1 > num2: {num1 > num2}")
    print(f"num1 < num2: {num1 < num2}")
    print(f"num1 >= num2: {num1 >= num2}")
    print(f"num1 <= num2: {num1 <= num2}")

def logic():
     num1 = bool(input("enter first boolen value : "))
     num2 = bool(input("enter second boolean value : "))
     print(f"num1 and num2: {num1 and num2}")
     print(f"num1 or num2: {num1 or num2}")
     print(f"not num1: {not num1}")

def bitwise():
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    print(f"num1 & num2: {num1 & num2}")
    print(f"num1 | num2: {num1 | num2}")
    print(f"num1 ^ num2: {num1 ^ num2}")
    print(f"~num1: {~num1}")
    print(f"num1 << 1: {num1 << 1}")
    print(f"num1 >> 1: {num1 >> 1}")

def special():
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    print(f"x is z: {x is z}")     
    print(f"x is y: {x is y}")     
    print(f"x == y: {x == y}")     
    print(f"x is not y: {x is not y}")

    print(f"1 in x: {1 in x}")
    print(f"4 not in x: {4 not in x}")

print("1. Arithmetic Operations \n2. Assignment Operations \n3. Comparison Operations \n4.Logical Operations \n5. Bitwise Operations \n6. Special Operations")
choice =int(input("enter your choice : "))
if choice == 1 :
    arithmetic()
elif choice ==2 :
    assignment()
elif choice ==3 :
    comparison()
elif choice == 4 :
    logic()
elif choice == 5:
    bitwise()
elif choice == 6 :
    special()
else:
    print("invalid choice")
