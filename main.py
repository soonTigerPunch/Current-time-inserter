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
   format_map={
    'year': "%Y",
    'mon': "%m",
    'day': "%d",
    'hour': "%H",
    'min': "%M",
    'sec': "%S",
    'ms': "%f" }
   parts = []
   for key, fmt in format_map.items():
       if format_vars[key].get():
            parts.append(fmt)
   time_format = '-'.join(parts)
   curr_time = datetime.now().strftime(time_format)
   insert_text(curr_time)


root = tk.Tk()
format_vars = { 
    'year': tk.BooleanVar(value=True),
    'mon': tk.BooleanVar(value=True),
    'day': tk.BooleanVar(value=True),
    'hour': tk.BooleanVar(value=True),
    'min': tk.BooleanVar(value=True),
    'sec': tk.BooleanVar(value=True),
    'ms': tk.BooleanVar(value=True) }


root.title("GUI")
root.geometry("350x275")
checkbox=tk.Checkbutton(root, text="년", variable=format_vars['year'])
checkbox.grid(row=0, column=0)
checkbox=tk.Checkbutton(root, text="월", variable=format_vars['mon'])
checkbox.grid(row=0, column=1)
checkbox=tk.Checkbutton(root, text="일", variable=format_vars['day'])
checkbox.grid(row=0, column=2)
checkbox=tk.Checkbutton(root, text="시", variable=format_vars['hour'])
checkbox.grid(row=0, column=3)
checkbox=tk.Checkbutton(root, text="분", variable=format_vars['min'])
checkbox.grid(row=0, column=4)
checkbox=tk.Checkbutton(root, text="초", variable=format_vars['sec'])
checkbox.grid(row=0, column=5)
checkbox=tk.Checkbutton(root, text="밀리초", variable=format_vars['ms'])
checkbox.grid(row=0, column=6           )

keyboard.add_hotkey('ctrl+space', lambda: insert_time_text()) 


root.mainloop()
