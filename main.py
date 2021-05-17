from tkinter import *
#модуль привязки
import sqlite3
#соединение с базой данных
conn = sqlite3.connect ('baza.db')
conn = sqlite3.connect ('Student.db')
#создаем курсор
cursor = conn.cursor
#переменная, которая выбирает рандомное число айди из базы данных с вопросами, для вывода в лейбл
rand = 'SELECT DICTINCT _id FROM baza ORDER BY RANDOM'
#код по визуалу

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
#название теста
        GLabel_560 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_560["font"] = ft
        GLabel_560["fg"] = "#333333"
        GLabel_560["justify"] = "center"
        GLabel_560["text"] = "Тест по предмету Алгоритмизация и программирование"
        GLabel_560.place(x=120, y=0, width=349, height=30)
#чекбокс
        GCheckBox_194=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_194["font"] = ft
        GCheckBox_194["fg"] = "#333333"
        GCheckBox_194["justify"] = "center"
        GCheckBox_194["text"] = "CheckBox1"
        GCheckBox_194.place(x=40,y=120,width=70,height=25)
        GCheckBox_194["offvalue"] = "0"
        GCheckBox_194["onvalue"] = "1"
        GCheckBox_194["command"] = self.GCheckBox_194_command
#кнопка проверки
        GButton_166=tk.Button(root)
        GButton_166["bg"] = "#dddddd"
        ft = tkFont.Font(family='Times',size=10)
        GButton_166["font"] = ft
        GButton_166["fg"] = "#000000"
        GButton_166["justify"] = "center"
        GButton_166["text"] = "Проверить"
        GButton_166.place(x=490,y=460,width=70,height=25)
        GButton_166["command"] = self.GButton_166_command
#вставка для вопроса
        GLabel_421=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_421["font"] = ft
        GLabel_421["fg"] = "#333333"
        GLabel_421["justify"] = "center"
        GLabel_421["text"] = ('SELECT vopros FROM baza WHERE _id = rand')
        GLabel_421.place(x=10,y=70,width=586,height=30)
#чекбокс
        GCheckBox_50=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_50["font"] = ft
        GCheckBox_50["fg"] = "#333333"
        GCheckBox_50["justify"] = "center"
        GCheckBox_50["text"] = "CheckBox2"
        GCheckBox_50.place(x=40,y=150,width=70,height=25)
        GCheckBox_50["offvalue"] = "0"
        GCheckBox_50["onvalue"] = "1"
        GCheckBox_50["command"] = self.GCheckBox_50_command
# чекбокс
        GCheckBox_906=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_906["font"] = ft
        GCheckBox_906["fg"] = "#333333"
        GCheckBox_906["justify"] = "center"
        GCheckBox_906["text"] = "CheckBox3"
        GCheckBox_906.place(x=40,y=180,width=70,height=25)
        GCheckBox_906["offvalue"] = "0"
        GCheckBox_906["onvalue"] = "1"
        GCheckBox_906["command"] = self.GCheckBox_906_command
#вставка второго вопроса
        GLabel_310=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_310["font"] = ft
        GLabel_310["fg"] = "#333333"
        GLabel_310["justify"] = "center"
        GLabel_310["text"] = "SELECT vopros FROM baza WHERE _id = rand"
        GLabel_310.place(x=10,y=220,width=581,height=30)
# чекбокс
        GCheckBox_21=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_21["font"] = ft
        GCheckBox_21["fg"] = "#333333"
        GCheckBox_21["justify"] = "center"
        GCheckBox_21["text"] = "CheckBox4"
        GCheckBox_21.place(x=40,y=270,width=70,height=25)
        GCheckBox_21["offvalue"] = "0"
        GCheckBox_21["onvalue"] = "1"
        GCheckBox_21["command"] = self.GCheckBox_21_command
# чекбокс
        GCheckBox_619=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_619["font"] = ft
        GCheckBox_619["fg"] = "#333333"
        GCheckBox_619["justify"] = "center"
        GCheckBox_619["text"] = "CheckBox5"
        GCheckBox_619.place(x=40,y=300,width=70,height=25)
        GCheckBox_619["offvalue"] = "0"
        GCheckBox_619["onvalue"] = "1"
        GCheckBox_619["command"] = self.GCheckBox_619_command
# чекбокс
        GCheckBox_119=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_119["font"] = ft
        GCheckBox_119["fg"] = "#333333"
        GCheckBox_119["justify"] = "center"
        GCheckBox_119["text"] = "CheckBox6"
        GCheckBox_119.place(x=40,y=330,width=70,height=25)
        GCheckBox_119["offvalue"] = "0"
        GCheckBox_119["onvalue"] = "1"
        GCheckBox_119["command"] = self.GCheckBox_119_command
#вставка вопроса
        GLabel_67=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_67["font"] = ft
        GLabel_67["fg"] = "#333333"
        GLabel_67["justify"] = "center"
        GLabel_67["text"] = "SELECT vopros FROM baza WHERE _id = rand"
        GLabel_67.place(x=20,y=370,width=571,height=30)

    def GCheckBox_194_command(self):
        print("command")


    def GButton_166_command(self):
        print("command")


    def GCheckBox_50_command(self):
        print("command")


    def GCheckBox_906_command(self):
        print("command")


    def GCheckBox_21_command(self):
        print("command")


    def GCheckBox_619_command(self):
        print("command")


    def GCheckBox_119_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


#закрываю соединение с базой данных
conn.close
