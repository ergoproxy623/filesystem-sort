from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extention = filename.split(".")
            print(extention)
            print(extention)
            if len(extention) > 1 and (extention[1].lower() == "fb2" or extention[1].lower() == "doc" or extention[1].lower() == "mp4"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)


folder_track = "/home/rox-9/trashbox"
folder_dest = "/home/rox-9/Video"
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
