from pathlib import Path

#Параметры
width = 1000
height = 800

#Шрифты
text_font = 'Zombie Holocaust'
mode_font = 'Comfortaa'

#Цвета
mainbg = '#202020'
labelbg = '#404040'
settingbg = '#606060'
fontcl = '#E0E0E0'
mode_clr = ['#990000','#00CC66']

#Состояния
modes = ['Offline','Online']
btn_mode = ['Start','Stop']

#Логика
observer = None
event_handler = None

#Картинки
settings = 'pics/settings.png'
close = 'pics/close.png'


#Ссылки
downloads = str(Path.home() / "Downloads")
music = str(Path.home() / "Music")

#Выбор
types = {
'music': music,
'images': None,
'videos': None
        }
h = 10
