import tkinter as tk
from tkinter import messagebox
#from pyfirmata import Arduino, PWM
#from time import sleep

#def blueLED():
#    delay = float(LEDtime.get())
#    brightness = float(LEDbright.get())
#    blueBtn.config(state = tk.DISABLED)
#    board.digital[3].write(brightness/100.0)
#    sleep(delay)
#    board.digital[3].write(0)
#    blueBtn.config(state = tk.ACTIVE)
#def redLED():
#    delay = float(LEDtime.get())
#    brightness = float(LEDbright.get())
#    redBtn.config(state = tk.DISABLED)
#    board.digital[4].write(brightness/99.9)
#    sleep(delay)
#    board.digital[4].write(0)#надо поменять когда придет время 4 на 5 а может и 6
#    redBtn.config(state = tk.ACTIVE)

def aboutMsg():
    messagebox.showinfo("Это программное обеспечение, которому все равно на логику\nLED Контроллер Вер 1.0\nJanuary 2026")

#   board = Arduino("COM3") 

#    board.digital[3].mode = PWM
#    board.digital[4].mode = PWM



#board = Arduino("COM3")

win = tk.Tk()
# Инициализация окна
win.title("Dimmer LED")
win.minsize(235, 150)

LEDtime = tk.Entry(win, bd=6, width=8)
LEDtime.grid(column=1, row=1)
# Создаем надписи label ну тип текст
label = tk.Label(win, text="Время свечения LED (сек").grid (column=2, row=1)
LEDbright = tk.Scale(win, bd=5, from_=0, to=100, orient=tk.HORIZONTAL)
tk.Label(win, text="Яркость LED")
label.grid(column =1, row = 1)
#кнопки вкл выкл делаем
BlueBtn = tk.Button(win, bd=4, text="BLUE LED") #command=blueLED)
BlueBtn.grid (column=1, row=3)
redBtn = tk.Button(win, bd=4, text="RED LED") #command=redLED)
redBtn.grid (column=1, row=3)
aboutBtn = tk.Button(win, text="Справка", command=aboutMsg)
aboutBtn.grid(column=1, row=4)
quitBtn = tk.Button(win, text="Выход") #command=win.quit)
quitBtn.grid(column=2, row=4)

win.mainloop()
