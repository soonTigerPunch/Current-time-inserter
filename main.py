import keyboard
import pyperclip
import pyautogui
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox, simpledialog


def insert_text(text: str):
    old_clip=pyperclip.paste()
    pyperclip.copy(text)
    time.sleep(0.05) 
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.05)
    pyperclip.copy(old_clip)
def insert_time_text():
    year='%Y'
    mon='%m'
    day='%d'
    hour='%H'
    min='%M'
    sec='%S'
    ms='%f'
    col=':'
    curr_time = datetime.now().strftime(f"{year}{col}{mon}{col}{day} {hour}{col}{min}{col}{sec}.{ms}")[:-3]
    insert_text(curr_time)
tk.Label( text="Press Shift+T to insert current time").pack(pady=20, padx=20)

root = tk.Tk()
root.title("GUI")
root.geometry("300x200")

keyboard.add_hotkey('alt+t', lambda: insert_time_text()) 

root.mainloop()