import tkinter as tk
from tkinter import messagebox
#from pyfirmata import Arduino, PWM
#from time import sleep

#
# def blueLED():
 #  delay = float(LEDtime.get())
 #  brightness = float(LEDbright.get())
  # blueBtn.config(state = tk.DISABLED)
  # board.digital[3].write(brightness/100.0)
  # sleep(delay)
  # board.digital[3].write(0)
  # blueBTN.config(state = tk.ACTIVE)
#def redLED():
  #  delay = float(LEDtime.get())
  #  brightness = float(LEDbright.get())
  #  redBtn.config(state = tk.DISABLED)
  #  board.digital[3].write(brightness/100.0)
   # sleep(delay)
    #board.digital[3].write(0)
    #redBTN.config(state = tk.ACTIVE)
def aboutMsg():
    messagebox.showinfo("Это программа обеспечение, которому все равно на логику\nLED Контроллер Вер 1.0\nJanuary 2026")

    

#board = Arduino("COM3")
#board.digital[3].mode = PWM
#board.digital[5].mode = PWM
# фигня собатий по blind
def exit_app(event=None):
    win.quit()

win = tk.Tk()
# Инициализация окна
win.title("Dimmer LED")
win.minsize(235, 150)
# новое из материала configure
win.configure(bg="#e6e6e6")

LEDtime = tk.Entry(win, bd=6, width=8, justify="center")
LEDtime.grid(column=1, row=1, padx=5, pady=5)

# Создаем надписи label ну тип текст
tk.Label(win, text="LED  ВКЛ Время(сек)").grid(column=2, row=1, padx=5)

LEDbright = tk.Scale(win, bd=5, from_=0, to=100, orient=tk.HORIZONTAL, length=120)
LEDbright.grid(column=1, row=2,padx=5, pady=5)

tk.Label(win, text="Яркость LED",bg="#e6e6e6").grid(column=2, row=2)
#кнопки вкл выкл делаем
Bluebtn = tk.Button(win, bd=4, text="Blue LED", activebackground="light blue") #command=blueLED)
Bluebtn.grid (column=1, row=3, pady=5)
redbtn = tk.Button(win, bd=4, text="RED LED", activebackground="pink") #command=redLED)
redbtn.grid (column=2, row=3, pady=5)
aboutBtn = tk.Button(win, text="Справка", command=aboutMsg)
aboutBtn.grid(column=1, row=4, pady=5)
quitBtn = tk.Button(win, text="Выйти", command=exit_app)
quitBtn.grid(column=2, row=4, pady=5)
win.bind("<Control-q>", exit_app) # Выход по Ctrl+q
win.bind("<Escape>", exit_app) # По esc
win.mainloop()