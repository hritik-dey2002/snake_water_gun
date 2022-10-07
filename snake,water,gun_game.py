import random

def gameWin(computer, you):
    if computer==you:
        return None
    elif computer=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif computer=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif computer=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    
print("computer's turn: snake(s) or water(w) or gun(g)")
randNo=random.randint(1, 3)
if randNo==1:
    computer='s'
elif randNo==2:
    computer='w'
elif randNo==3:
    computer='g'

you=input("your's turn: snake(1) or water(2) or gun(3)")
a=gameWin(computer, you)

print(f"computer choice {computer}")
print(f"your choice {you}")

if a==None:
    print("The match is tie")
elif a:
    print("you are win")
else:
    print("you lose!")