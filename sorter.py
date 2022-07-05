import os
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import time
from GUI import *
from config import *

class Handler(FileSystemEventHandler):
    def __init__(self,sort_path,user_dir):
        self.sort_path=sort_path
        self.user_dir=user_dir
    def on_modified(self,event):
        for file in os.listdir(path=self.sort_path):
            extension = os.path.splitext(file)[-1]
            src = self.sort_path + '\\' + file
            if extension == '.mp3':
                dst = self.user_dir + '\\' + file
                try:
                    os.rename(src,dst)
                except:
                    pass

sort_path = str(Path.home() / "Downloads")
user_dir = str(Path.home() / "Music")

def watching():
    observer.schedule(event_handler,sort_path,recursive = False)
    observer.start()

def unwatching():
    observer.stop()
    observer.join()

#observer = None
#event_handler = None

def start():
    global bool_mode, observer, event_handler
    bool_mode = not(bool_mode)

    cure_mode.config(text=modes[bool_mode],fg=mode_clr[bool_mode])
    btn_1.config(text=btn_mode[bool_mode])
    if bool_mode:
        observer = PollingObserver()
        event_handler = Handler(sort_path,user_dir)
        watching()
    else:
        unwatching()

btn_1.config(command=start)
main()
