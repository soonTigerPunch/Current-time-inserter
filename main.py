import keyboard
import pyperclip
import pyautogui
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox, simpledialog,StringVar
import json
import pystray
from pystray import MenuItem , Menu
from PIL import Image, ImageDraw
import threading


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
    new_hotkey = simpledialog.askstring("핫키 바꾸기", "바꾸실 핫키를 입력하세요. (예: ctrl+shift+t):")
    if new_hotkey:
        try:
            keyboard.remove_hotkey(current_hotkey)
            keyboard.add_hotkey(new_hotkey, lambda: insert_time_text())
            current_hotkey = new_hotkey
            hotkey_label.config(text="현재 핫키: " + current_hotkey)
        except Exception as e:
            messagebox.showerror("오류", f"핫키 설정 실패: {e}")
    save_config()

def save_config():
    config = {
        'hotkey': current_hotkey,
        'format': { key: var.get() for key, var in format_vars.items() },
        'separator': Separator_input.get()
    }
    with open('config.json', 'w') as f:
        json.dump(config, f)
def load_config():
    global current_hotkey
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            current_hotkey = config.get('hotkey', current_hotkey)
            for key, value in config.get('format', {}).items():
                if key in format_vars:
                    format_vars[key].set(value)
            Separator_input.set(config.get('separator', Separator_input.get()))
    except FileNotFoundError:
        pass
def run_tray():
    
    def show_window(icon, item):
        root.deiconify()
    
    def on_quit(icon, item):
        save_config()
        icon.stop()
        root.quit()
    
    menu = Menu(
        MenuItem("종료", on_quit),
        MenuItem("설정 열기", show_window)
    )
    image = Image.open("clock.png")
    
    icon = pystray.Icon("현재 시간 삽입기", image, "Time Inserter", menu)
    
    icon.run()
        


root = tk.Tk()

format_vars = { 
    'year': tk.BooleanVar(value=True,),
    'mon': tk.BooleanVar(value=True),
    'day': tk.BooleanVar(value=True),
    'hour': tk.BooleanVar(value=True),
    'min': tk.BooleanVar(value=True),
    'sec': tk.BooleanVar(value=True),
    'ms': tk.BooleanVar(value=True) }

Separator_input=StringVar(value="/")
load_config()
tk.OptionMenu(root, Separator_input, "/", "-", ".", ":",).place(x=10, y=35)
change_hotkey_button=tk.Button(root, text="핫키 변경", command=lambda: change_hotkey())
change_hotkey_button.place(x=170, y=248)
hotkey_label=tk.Label(root, text="현재 핫키: " + current_hotkey)
hotkey_label.place(x=5, y=250)

root.title("현재 시간 삽입기")
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




tray_thread = threading.Thread(target=run_tray, daemon=True)
tray_thread.start()

root.withdraw()
root.mainloop()
