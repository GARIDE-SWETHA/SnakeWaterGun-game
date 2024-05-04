import random 
def gamewin(comp,you):
    if comp==you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True   
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True        
print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randno=random.randint(1,3)
print(randno)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
    

you=input("player's Turn: Snake(s) Water(w) or Gun(g)?\n")
a=gamewin(comp,you)
if a==None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You loose!")
