import os
from fuzzywuzzy import fuzz
import pyttsx3
import webbrowser
from shutdown import shutdown, restart
from pyautogui import hotkey
import json

# Загрузка JSON
with open("configs.json", "r", encoding="utf-8") as f:
    ops = json.load(f)

apps = ops["apps"]

# Вывод всех приложений
for name, path in apps.items():
    print(f"{name} -> {path}")

# Голосовой движок
engine = pyttsx3.init()
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Запуск программ
def StartProgram(cmd):
    cmd = cmd.lower().strip()
    bestRatio = 0
    bestProgram = None

    for program in apps:
        ratio = fuzz.partial_ratio(program.lower(), cmd)
        if ratio > bestRatio:
            bestRatio = ratio
            bestProgram = program

    if bestRatio > 65:
        exe = os.path.expandvars(apps[bestProgram])
        speak(f"Запускаю! {bestProgram}")
        os.system(f'Start "" "{exe}"')
    else:
        speak("Приложение не найдено.")

# Системные команды
def TryExecuteCommand(cmd):
    text = cmd.lower().strip()

    if "комп'ютер" in text:
        speak("Выключаю!")
        shutdown()
        return True

    if "перезапусти комп'ютер" in text:
        speak("Перезапускаю!")
        restart()
        return True

    if "панель задач" in text:
        speak("Открываю!")
        hotkey("winleft")
        return True

    if "ютуб" in text:
        speak("Запускаю YouTube!")
        webbrowser.open_new_tab("https://www.youtube.com")
        return True

    if "выйди из кс" in text or "закрой кс" in text:
        speak("Закрываю CS:GO")
        os.system('taskkill /f /im cs2.exe')
        return True

    if "выйди с дискорд" in text or "закрой дс" in text:
        speak("Закрываю Discord")
        os.system('taskkill /f /im Discord.exe')
        return True

    if "отключись" in text:
        speak("Отключаюсь.")
        return True

    return False

# Приветствие
speak("Здравствуйте, я голосовой ассистент Lume, чем могу помочь?")

# Главный цикл
while True:
    cmd = input(">> ").lower()
    
    if TryExecuteCommand(cmd):
        if "отключись" in cmd:
            break
    else:
        StartProgram(cmd)
