import pyautogui
import keyboard
import time

def locate_image(img):
    cords_image = pyautogui.locateOnScreen(img, confidence=0.7)
    if cords_image is not None:
        # print(cords_image)
        cords_center = pyautogui.center(cords_image)
        pyautogui.click(cords_center)
        time.sleep(0.2)
        return True
    else:
        time.sleep(0.1)
        pyautogui.moveTo(100, 100)
        return False
    
def check_for_exit_combination():
    # Verifica se a combinação Ctrl + Alt + C foi pressionada para sair do script.
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('c'):
        print("Combinação de saída detectada, terminando o script.")
        exit()

while True:
    check_for_exit_combination()
    test = locate_image('images/tres.png')
    if test is True:
        test = locate_image('images/sair.png')
        if test:
            locate_image('images/sim.png')
        else:
            print("nao localizado sair")
    else:
        print("nao localizado tres")   
