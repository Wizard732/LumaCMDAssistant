Luma is a simple voice assistant written in Python that allows you to launch applications, open websites, and execute basic commands using text input.

Features

Launch applications (Steam, Discord, Telegram, Spotify, etc.)

Quick access to YouTube

Shut down and restart your computer

Close applications (e.g., CS:GO, Discord)

Customizable commands and assistant names

Installation

Clone the repository

git clone https://github.com/ваш-репозиторий/Luma.git

Install libraries

pip install pyttsx3 fuzzywuzzy python-Levenshtein pyautogui

Before running, change the paths to applications in the Luma.py file for your computer. For example:

“steam”: r“C:\Program Files (x86)\Steam\steam.exe”

If the path is different on your PC, replace it with the correct one.

Run the assistant:

python Luma.py

Usage

Enter the command in the console or via the GUI.

Lum, turn on Steam. Lum, open YouTube.

The “disconnect” command terminates the assistant.

You can use the buttons in the GUI to quickly launch applications.

Notes

Be sure to adjust the path to the applications for your computer.

Works on Windows.

Translated with DeepL.com (free version)
