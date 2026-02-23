import keyboard
import pyperclip
import pyautogui
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox, simpledialog,StringVar

current_hotkey = 'ctrl+space'
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
   time_format = Separator_input.get().join(parts)
   curr_time = datetime.now().strftime(time_format)
   if '%f' in time_format:
        curr_time = curr_time[:-3]
   insert_text(curr_time)
def change_hotkey():
    global current_hotkey
    new_hotkey = simpledialog.askstring("Change Hotkey", "Enter new hotkey (e.g., ctrl+shift+t):")
    if new_hotkey:
        try:
            keyboard.remove_hotkey(current_hotkey)
            keyboard.add_hotkey(new_hotkey, lambda: insert_time_text())
            current_hotkey = new_hotkey
            hotkey_label.config(text="Current Hotkey: " + current_hotkey)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to set hotkey: {e}")
        


root = tk.Tk()

format_vars = { 
    'year': tk.BooleanVar(value=True),
    'mon': tk.BooleanVar(value=True),
    'day': tk.BooleanVar(value=True),
    'hour': tk.BooleanVar(value=True),
    'min': tk.BooleanVar(value=True),
    'sec': tk.BooleanVar(value=True),
    'ms': tk.BooleanVar(value=True) }

Separator_input=StringVar(value="/")
tk.OptionMenu(root, Separator_input, "/", "-", ".", ":",).place(x=10, y=35)
change_hotkey_button=tk.Button(root, text="Change Hotkey", command=lambda: change_hotkey())
change_hotkey_button.place(x=170, y=248)
hotkey_label=tk.Label(root, text="Current Hotkey: " + current_hotkey)
hotkey_label.place(x=5, y=250)


root.title("current time inserter")
root.geometry("350x275")
root.resizable(False, False)
checkbox=tk.Checkbutton(root, text="년", variable=format_vars['year'])
checkbox.place(x=10, y=10)
checkbox=tk.Checkbutton(root, text="월", variable=format_vars['mon'])
checkbox.place(x=50, y=10)
checkbox=tk.Checkbutton(root, text="일", variable=format_vars['day'])
checkbox.place(x=90, y=10)
checkbox=tk.Checkbutton(root, text="시", variable=format_vars['hour'])
checkbox.place(x=130, y=10)
checkbox=tk.Checkbutton(root, text="분", variable=format_vars['min'])
checkbox.place(x=170, y=10)
checkbox=tk.Checkbutton(root, text="초", variable=format_vars['sec'])
checkbox.place(x=210, y=10)
checkbox=tk.Checkbutton(root, text="밀리초", variable=format_vars['ms'])
checkbox.place(x=250, y=10)



keyboard.add_hotkey(current_hotkey, lambda: insert_time_text()) 


root.mainloop()
