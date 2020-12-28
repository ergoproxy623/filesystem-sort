from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            file_name,  extention = os.path.splitext(filename)
            if len(extention) > 1 and extention in ext_list:
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)


folder_track = "/home/rox-9/trashbox"
folder_dest = "/home/rox-9/Video"
ext_list = [".fb2", ".mp4"]

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
