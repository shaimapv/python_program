def vowels(string1):
    count_vowels=0
    count_consonant=0
    for i in string1:
        if i in ["a","e","i","o","u"]:
            count_vowels=count_vowels+1
        else:
            count_consonant=count_consonant+1
    print("number of vowels = ",count_vowels)
    print("number of consonant = ",count_consonant)


def pallindrome(string1):
    if string1 == string1[::-1] :
        print("string is a pallindrome")
    else:
        print("string is not a pallindrome")

def frequency(string1):
    count={}
    for i in string1:
        if i in count :
            count[i]=count[i]+1
        else:
            count[i]=1
    for i in set(string1):
        print("count of ",i, "is ",count[i] )
string1 = input("enter a string : ").lower()
print("1:number of vowels and consonants \n2:is pallindrome or not \n3:frequency of letters")
choice = int(input("enter your choice : "))
if choice == 1:
    vowels(string1)
elif choice == 2:
    pallindrome(string1)
elif choice == 3:
    frequency(string1)
else :
    print("invalid choice")


    








    


