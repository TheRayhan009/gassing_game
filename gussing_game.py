import random
import os
class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    
point=0
first_txt=0
def start():
    # this is the welcome text.You will see this text first when you start playing this game.

    start1='''
    
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
    big_and_bold_text = color.BOLD + start1.upper() + color.END
    print(big_and_bold_text)

def play_or_not():
    # This is a text asking you want to play again or not .
    play='''
    
____________________________________________________________________________________________________________
|                                          You want to play again?                                          |
|                                               To yes press (y)                                            |           
|                                               To no press (n)                                             |
|___________________________________________________________________________________________________________|
'''
    big_and_bold_text = color.BOLD + play.upper() + color.END
    print(big_and_bold_text)
def gogo():
    # This text will appear whenever you answer yes(y) to you want to play again.
    play='''
    
____________________________________________________________________________________________________________
|                                          let's Goooo!!                                                    |           
|___________________________________________________________________________________________________________|
'''
    big_and_bold_text = color.BOLD + play.upper() + color.END
    print(big_and_bold_text)
    
while True:
    the_gussing_numbre=random.randint(1 , 1000)
    x=30
    q=0
    if first_txt==0:
        start()
    else:
        gogo()
    while x>0:
        x-=1
        first_txt=1
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
            print("Charles Remaining",x)
        
    if q==0:
        point=0
        print("\n \n You defeated..!!  your point is : ",point)
        play_or_not()
        yes_or_no=input()
        if yes_or_no=="n" or yes_or_no=="N":
            print("The game is sucsecfully ended.!")
            break
        if yes_or_no=="y"or yes_or_no=="Y":
            continue
        else:
            print("error : Invalid input")
            break
    elif q==1:
        print("you got it!! your point is : ",point)
        play_or_not()
        yes_or_no=input()
        if yes_or_no=="n" or yes_or_no=="N":
            print("The game is sucsecfully ended.!")
            break
        if yes_or_no=="y"or yes_or_no=="Y":
            continue
        else:
            print("error : Invalid input")
            break
            
