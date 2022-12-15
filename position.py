import pyautogui as pg
import keyboard as kb
from time import sleep


def position() :
    x, y = pg.position()
    obj = open('position.txt','a')
    #obj.write("x = "+str(x)+" y = "+str(y))
    obj.write(f"x = {x} y = {y} \n ") 
    obj.close()
    position_ = f"{x}, {y}"
    print("Position ok", position_)
    sleep(1)

##teste 1
#sleep(5)
#position()

#teste 2
def initial() :
    print("""
    Aguardando...
    Pressione "A" para position.
    Pressione "Esc" para sair.
    """)


initial()

while True:

    if kb.is_pressed('a'):
        position()
        continue
   
    if kb.is_pressed('esc'):
        print("Exit.")
        break
   
        




    
    

