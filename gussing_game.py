import random
import os
point=0
koko=0
def start():
    start1='''
    # this is the welcome text.You will see this text first when you start playing this game.
____________________________________________________________________________________________________________
|                                              WELCOME!!                                                    |
|                                   This is a numbre gussing game.                                          |
|                                       The numbers are 1 - 1000                                            |
|                                      You have 30 chance to guss.                                          |
|                                                                                                           |
|                                              --info--                                                     |
|                                        The game made by TheRayhan PY .                                    |
|                                    Bilding programming lenguage is python.                                |
|                                                ENJOY!!                                                    |
|___________________________________________________________________________________________________________|
'''
    print(start1)

def play_or_not():
    play='''
    # This is a text asking you want to play again or not .
____________________________________________________________________________________________________________
|                                          You want to play again?                                          |
|                                               To yes press (y)                                            |           
|                                               To no press (n)                                             |
|___________________________________________________________________________________________________________|
'''
    print(play)
def gogo():
    play='''
    # This text will appear whenever you answer yes(y) to you want to play again.
____________________________________________________________________________________________________________
|                                          let's Goooo!!                                                    |           
|___________________________________________________________________________________________________________|
'''
    print(play)
    
while True:
    the_gussing_numbre=random.randint(1 , 1000)
    x=0
    q=0
    if koko==0:
        start()
    else:
        gogo()
    while x<30:
        koko=1
        num=int(input())
        if num==the_gussing_numbre:
            q=1
            point+=1
            break
        else:
            print("it's not right.!")
            if num>the_gussing_numbre:
                print("it's too long.")
            elif num<the_gussing_numbre:
                print("it's too small.")
        x+=1
    if q==0:
        point=0
        print("\n \n You defeated..!!  your point is : ",point)
        play_or_not()
        yorno=input()
        if yorno=="n":
            print("The game is sucsecfully ended.!")
            break
        if yorno=="y":
            continue
        else:
            print("error : Invalid input")
            break
    elif q==1:
        print("you got it!! your point is : ",point)
        play_or_not()
        yorno=input()
        if yorno=="n":
            print("The game is sucsecfully ended.!")
            break
        if yorno=="y":
            continue
        else:
            print("error : Invalid input")
            break
            
