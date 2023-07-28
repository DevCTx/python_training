import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileObserver(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path == shared_file_path:
            print("Program 2: File modified!")
            # Add your code to respond to the file modification here.


if __name__ == "__main__":
    shared_file_path = os.path.abspath("shared_file.txt")

    event_handler = FileObserver()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(shared_file_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
