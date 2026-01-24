import tkinter as tk
from tkinter import messagebox
from pyfirmata import Arduino, PWM
from time import sleep

# Функционал 

def blueLED():
    delay = float(LEDtime.get())
    brightness = float(LEDbright.get())

    blueBtn.config(state=tk.DISABLED)
   # board.digital[3].write(brightness / 100.0)
    sleep(delay)
    #board.digital[3].write(0)
    blueBtn.config(state=tk.ACTIVE)


def redLED():
    delay = float(LEDtime.get())
    brightness = float(LEDbright.get())

    redBtn.config(state=tk.DISABLED)
    #board.digital[5].write(brightness / 100.0)
    sleep(delay)
    #board.digital[5].write(0)
    redBtn.config(state=tk.ACTIVE)


def aboutMsg():
    messagebox.showinfo(
        "О программе",
        "LED Контроллер v1.0\nJanuary 2026\n\nРабота с хуевым Perduino через Python"
    )

# Пердуино

#board = Arduino("COM3")

#board.digital[3].mode = PWM
#board.digital[5].mode = PWM

# наше окошечко

win = tk.Tk()
#win.title("Dimmer LED")
#win.geometry("320x240")
#win.resizable(False, False)
#win.configure(bg="#1e1e2f")

# Шрифтс

font_title = ("Gabriola", 26, "bold")
font_text = ("Segoe Script", 12, "bold")
font_btn = ("Segoe Script", 11, "bold")

# Заголовок

tk.Label(
    win,
    text="LED CONTROLLER",
    font=font_title,
    fg="white",
    bg="#1e1e2f"
).grid(column=1, row=0, columnspan=2, pady=10)

# Ввод данных

tk.Label(
    win,
    text="Время (сек)",
    font=font_text,
    fg="white",
    bg="#1e1e2f"
).grid(column=1, row=1, sticky="w")

LEDtime = tk.Entry(
    win,
    width=10,
    font=font_text,
    bg="#2a2a40",
    fg="white",
    insertbackground="white",
    relief="flat"
)
LEDtime.grid(column=2, row=1)

tk.Label(
    win,
    text="Яркость",
    font=font_text,
    fg="white",
    bg="#1e1e2f"
).grid(column=1, row=2, sticky="w")

LEDbright = tk.Scale(
    win,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    bg="#1e1e2f",
    fg="white",
    highlightthickness=0,
    troughcolor="#2a2a40"
)
LEDbright.grid(column=2, row=2)

# Кнопочки

blueBtn = tk.Button(
    win,
    text="BLUE LED",
    font=font_btn,
    bg="#3b82f6",
    fg="blue",
    relief="flat",
    width=12,
    command=blueLED
)
blueBtn.grid(column=1, row=3, pady=10)

redBtn = tk.Button(
    win,
    text="RED LED",
    font=font_btn,
    bg="#ef4444",
    fg="red",
    relief="flat",
    width=12,
    command=redLED
)
redBtn.grid(column=2, row=3)

aboutBtn = tk.Button(
    win,
    text="Справка",
    font=font_btn,
    bg="#22c55e",
    fg="green",
    relief="flat",
    width=12,
    command=aboutMsg
)
aboutBtn.grid(column=1, row=4, pady=5)

quitBtn = tk.Button(
    win,
    text="Закрыть",
    font=font_btn,
    bg="#6b7280",
    fg="gray",
    relief="flat",
    width=12,
    command=win.quit
)
quitBtn.grid(column=2, row=4)

win.mainloop()
