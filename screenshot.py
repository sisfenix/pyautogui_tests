import pyautogui
from PIL import Image

im2=pyautogui.screenshot("newone.png")
Image.open("newone.png").convert("RGB").save("newone.png")