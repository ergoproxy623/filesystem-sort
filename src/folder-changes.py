import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(__name__)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    print(sys.argv)
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(path)
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, '/home/rox-9/trashbox', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
