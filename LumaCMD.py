import tkinter as tk
from Luma import StartProgram, Command, speak  

def on_command():
    cmd = entry.get().strip().lower()
    entry.delete(0, tk.END)
    if cmd == "отключись":
        speak("Отключаюсь.")
        root.destroy()
        return
    if not Command(cmd):
        StartProgram(cmd)

root = tk.Tk()
root.title("Luma Assistant")
root.geometry("400x250")

label = tk.Label(root, text="Введите команду для Luma:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Выполнить", command=on_command)
button.pack(pady=10)

def run_youtube():
    StartProgram("ютуб")

def run_steam():
    StartProgram("steam")

youtube_btn = tk.Button(root, text="Открыть YouTube", command=run_youtube)
youtube_btn.pack(pady=5)

steam_btn = tk.Button(root, text="Открыть Steam", command=run_steam)
steam_btn.pack(pady=5)

root.mainloop()
