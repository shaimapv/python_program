def run_quiz(level):
    score =0 
    for i in level :
        print("\n",i['questions'])
        for j in i['options']:
            print(j)

        answer = input("enter answer(A/B/C/D) :").upper()
        if answer not in ['A','B','C','D']:
            print("invalid answer ")
            continue
        if answer==i['answer']:
            score+=1
            print("answer is correct ")
        else:
            print("wrong answer")

    print(f"score is {score}")
    print("\nExcellent"if score==3 else "\ngood try" )
    return score
level1=[{'questions':'what is capital of india ?','options':['A.Mumbai','B.Delhi','C.Kolkata','D.Lucknow'],'answer':'B'},
        {'questions':'2+2=?','options':['A.5','B.4','C.3','D.6'],'answer':'B'},
        {'questions':'Which is a programming language?','options':['A.python','B.snake','C.django','D.http'],'answer':'A'}]

level2=[{'questions':'which gas is most abundant in earth\'s atmosphere ?','options':['A.Oxygen','B.Nitrogen','C.Hydrogen','D.Carbon Dioxide'],'answer':'B'},
        {'questions':'In which year did india become a republic ?','options':['A.1947','B.1950','C.1952','D.1949'],'answer':'B'},
        {'questions':'which city is known as \'city of canals\' ?','options':['A.Amsterdam','B.Bangkok','C.Bruges','D.Venice'],'answer':'D'}]
level3=[{'questions':'In 2023, which tech company introduced the AI tool named "Bard" as a competitor to ChatGPT ?','options':['A.Microsoft','B.Google','C.Amazon','D.Metaw'],'answer':'B'},
        {'questions':'which vitamin is primarily obtained from sunlight ?','options':['A.vitamin A','B.vitamin B12','C.vitamin C','D.vitamin D'],'answer':'D'},
        {'questions':'RAM is a type of?','options':['A. Storage', 'B. Input', 'C. Output', 'D. Memory'], 'answer': 'D'}]

print("Wlcome to quiz game ")
name=input("enter your name : ")

while(True):
    print(f"hello {name} , let's start the game ")

    print("\n---level 1---")
    score1 = run_quiz(level1)
    if score1<2:
        print("you failed level 1 ,try again later")
        break
    print("\n---level 2---")
    score2 = run_quiz(level2)
    if score2<2:
        print("you failed level 2 , Game over")
        break
    print("\n---level 3---")
    score3 = run_quiz(level3)
    if score3<2:
        print("you failed level 3 , Game over")
        break
    print("Congratulation , you completed all levels")

    choice = input("Do you want to play again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing!")
        break

"""
Output:
PS C:\training\5th task> python quiz_game.py
Wlcome to quiz game 
enter your name : adam
hello adam , let's start the game 

---level 1---

 what is capital of india ?
A.Mumbai
B.Delhi
C.Kolkata
D.Lucknow
enter answer(A/B/C/D) :B
answer is correct 

 2+2=?
A.5
B.4
C.3
D.6
enter answer(A/B/C/D) :B
answer is correct 

 Which is a programming language?
A.python
B.snake
C.django
D.http
enter answer(A/B/C/D) :A
answer is correct 
score is 3

Excellent

---level 2---

 which gas is most abundant in earth's atmosphere ?
A.Oxygen
B.Nitrogen
C.Hydrogen
D.Carbon Dioxide
enter answer(A/B/C/D) :B
answer is correct

 In which year did india become a republic ?
A.1947
B.1950
C.1952
D.1949
enter answer(A/B/C/D) :B
answer is correct

 which city is known as 'city of canals' ?
A.Amsterdam
B.Bangkok
C.Bruges
D.Venice
enter answer(A/B/C/D) :D
answer is correct
score is 3

Excellent

---level 3---

 In 2023, which tech company introduced the AI tool named "Bard" as a competitor to ChatGPT ?
A.Microsoft
B.Google
C.Amazon
D.Metaw
enter answer(A/B/C/D) :B
answer is correct

 which vitamin is primarily obtained from sunlight ?
A.vitamin A
B.vitamin B12
C.vitamin C
D.vitamin D
enter answer(A/B/C/D) :D
answer is correct

 RAM is a type of?
A. Storage
B. Input
C. Output
D. Memory
enter answer(A/B/C/D) :d
answer is correct
score is 3

Excellent
Congratulation , you completed all levels
Do you want to play again? (y/n): n
Thanks for playing!"""



