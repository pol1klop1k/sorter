import tkinter as tk
import config as cfg
from tkinter import filedialog


#Function
def cls(l):                     #Функция закрытия окна настроек
    for i in l:
        i.destroy()

def choose(path, type):                               #Функция выбора пути для сортировки
    win.dirname = filedialog.askdirectory()
    if win.dirname != '':
        cfg.types[type] = win.dirname
    print(cfg.types)



def set():              #Функция вызова окна настроек
    toClose = []#Лист со всеми виджетами, которые надо закрыть

    prop = tk.Label(win,
                    bg=cfg.settingbg,
                    width=200,
                    height=cfg.height)
    prop.place(x=700, y=28)
    toClose.append(prop)

    musiclab = tk.Label(win,
                        text='Music',
                        bg=cfg.settingbg,
                        fg=cfg.mainbg,
                        font=(cfg.text_font, 20))
    musiclab.place(x=730, y=50)
    toClose.append(musiclab)

    music = tk.Button(win,
                    text='Change',
                    command=lambda: choose(cfg.music, 'music'),
                    width=15
                    )
    music.place(x=840, y=58)
    toClose.append(music)

    close = tk.Button(win,
                    image=closebtn,
                    command=lambda: cls(toClose),
                    borderwidth=0,
                    bg=cfg.settingbg,
                    activebackground=cfg.settingbg)
    close.place(x=980, y=30)
    toClose.append(close)



win = tk.Tk()
win.title('Sorter')#Название программы
win.geometry(f'{cfg.width}x{cfg.height}+10+10')
win.config(bg=cfg.mainbg)



closebtn = tk.PhotoImage(file=cfg.close)

#FOOTER
footer_label = tk.Label(win,
                    text='Sorter', #Текст
                    bg=cfg.labelbg,   #Цвет окна
                    fg=cfg.fontcl,   #Цвет шрифта
                    font=(cfg.text_font,14),   #Шрифт
                    padx=20,   #Отступ по х
                    width=cfg.width, #Ширина
                    height=1, #Высота
                    anchor='nw',#расположение текста,
                    )
footer_label.pack()

#Mode
cure_mode = tk.Label(win,
                    text = 'Offline',
                    bg=cfg.mainbg,
                    fg='#990000', #красный
                    font=(cfg.mode_font,40),
                    width=300,
                    height=10,
                    justify='center')
cure_mode.pack()

#Button
btn_1 = tk.Button(win,
                text = 'Start',
                height=2,
                width=25)
btn_1.pack()
bool_mode = 0

#Settings
img_btn = tk.PhotoImage(file=cfg.settings)

options = tk.Button(win,
                    image=img_btn,
                    width=40,
                    height=40,
                    borderwidth=0,
                    bg=cfg.mainbg,
                    activebackground=cfg.mainbg,
                    command=set)
options.place(x=930, y=50)


def main():
    win.mainloop()
