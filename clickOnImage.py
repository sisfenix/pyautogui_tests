import pyautogui
import keyboard
import time

def check_for_exit_combination():
    # Verifica se a combinação Ctrl + Alt + C foi pressionada para sair do script.
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('c'):
        print("Combinação de saída detectada, terminando o script.")
        exit()

def locate_image():
    cords_image = pyautogui.locateOnScreen('nao.png', confidence=0.7)
    cords_center = pyautogui.center(cords_image)
    print(cords_image, cords_center)
    pyautogui.click(cords_center)
    time.sleep(1)

def locate_image_loop():
    while True:
        check_for_exit_combination()
        cords_image = pyautogui.locateOnScreen('images/nao.png', confidence=0.7)
        if cords_image is not None:
            print(cords_image)
            cords_center = pyautogui.center(cords_image)
            pyautogui.click(cords_center)
        else:
            print("nao localizado")

        time.sleep(0.1)
        
locate_image_loop()
