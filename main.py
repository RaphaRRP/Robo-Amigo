import pyautogui
import time
import pyautogui
import time
from pytesseract import pytesseract
import webbrowser


pytesseract.tesseract_cmd = r'C:/Users/prr8ca/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

left, top = 1360, 740
width, height = 1870 - 1360, 968 - 740


def open_timer():
    url = "https://relogioonline.com.br/temporizador/#countdown=00:00:01&enabled=0&seconds=1&sound=happy&loop=1"
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.click(x=1220, y=735)


def check_for_new_messages():
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    text = pytesseract.image_to_string(screenshot)
    return text

last_message = ""

while True:
    pyautogui.moveTo(x=1500, y=300, duration=1)
    pyautogui.moveTo(x=500, y=300, duration=1)
    
    new_message = check_for_new_messages()
    if new_message.strip() and new_message != last_message:
        print("mensagem recebida")
        last_message = new_message
        open_timer()
        break
    time.sleep(1)

