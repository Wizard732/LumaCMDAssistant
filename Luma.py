import os
from fuzzywuzzy import fuzz
import pyttsx3
import webbrowser
from shutdown import shutdown, restart
from pyautogui import hotkey

# TODO:
# General comments:
# 1) Move "opps" to a separate json file with name "configs.json" and read these configs from here. Do not aks user actually to modify the code (bad practice because User can accidentally break the code).
# 2) Transalte everything to English
# 3) Create "requirements.txt" file and use it to install all required dependencies.
# 4) Use virtual envs in Python
# 5) Translate README.md to English as well



opps = {
    "name":{"Лум","Лим","Лем","Лумс","Lum","Luma","Lumas","Лума",},
    "command":{"Включи","Выключи","Запусти","Закрой","Отключи","Выйди","Открой","Ливни",},
    "apps": {
      # TODO: If User should modify only these "apps" section then move only this section to "configs.json"
        "steam": r"C:\Program Files (x86)\Steam\steam.exe",
        "стим": r"C:\Program Files (x86)\Steam\steam.exe",

        "браузер": r"C:\Users\bvdov\AppData\Local\Programs\Opera GX\opera.exe",
        "хром":    r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        "дискорд": r"C:\Users\bvdov\AppData\Local\Discord\app-1.0.9214\Discord.exe",
        "discord": r"C:\Users\bvdov\AppData\Local\Discord\app-1.0.9214\Discord.exe", #пути до приложений 

        "telegram": r"C:\Users\%USERNAME%\AppData\Roaming\Telegram Desktop\Telegram.exe",
        "телеграм": r"C:\Users\%USERNAME%\AppData\Roaming\Telegram Desktop\Telegram.exe",

        "спотифи":  r"C:\Users\bvdov\AppData\Roaming\Spotify\Spotify.exe",
        "спотифай": r"C:\Users\bvdov\AppData\Roaming\Spotify\Spotify.exe",

        "кс": r"steam://rungameid/730",
        "кс го": r"steam://rungameid/730",

        "вар тандер": r"steam://rungameid/236390",
        "War Thunder": r"steam://rungameid/236390",

    }
}

engine = pyttsx3.init() #создаем голос
def speak(text):
        print(text) #выводим голос в консоль
        engine.say(text) #заставляем озвучить голос
        engine.runAndWait() #запуск


def StartProgram(cmd):
        cmd = cmd.lower().strip()

        bestRatio = 0
        bestProgram = None

        for program in opps["apps"]:
             ratio = fuzz.partial_ratio(program, cmd) #проверяем какое приложение самое похожее 
             if (ratio > bestRatio):
                    bestRatio = ratio 
                    bestProgram = program #добавляем в переменные данные

        if(bestRatio > 65):
                exe = opps["apps"][bestProgram]
                speak(f"Запускаю! {bestProgram}") #нашли самую похожую команду запускаем ее
                os.system(f'Start "" "{exe}"')
                
        else:
            speak("Приложение не найдено.")

# TODO: rename to "TryExecuteCommand" for more obvious function purpose
def Command(cmd):
      text = cmd.lower().strip()

      if ("комп'ютер" in text):
            speak("Выключаю!")
            shutdown()
            return True

      if ("перезапусти комп'ютер" in text):
            speak("Перезапускаю!")
            restart()
            return True

      if ("панель задач" in text):
            speak("Открываю!")
            hotkey("winleft")
            return True
      
      if ("ютуб" in text):
        speak("Запускаю YouTube!") #запуск ютуб
        webbrowser.open_new_tab("https://www.youtube.com")
        return True
    
     
      if "выйди из кс" in text or "закрой кс" in text:
        speak("Закрываю CS:GO")
        os.system('taskkill /f /im  cs2.exe')  
        return True
      
    
      if "выйди с дискорд" in text or "закрой дс" in text:
        speak("Закрываю Discord")
        os.system('taskkill /f /im Discord.exe')  
        return True
      
      if "отключись" in text:
            speak("Отключаюсь.")
            return True  

      return False 

speak("Здраствуйте, я голосовой ассистент Lume, чем могу помочь?")

while True:
    cmd = input(">> ").lower()
    
    if ("отключись" in cmd):
        speak("Отключаюсь.")
        break  # программа завершится
    
    if not Command(cmd):
        StartProgram(cmd)