from __future__ import print_function
import time
import sys
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import fileReader
import pydicom
from ftp.ftp import upload
from multiprocessing import Process

class CrtHandler(PatternMatchingEventHandler):
    patterns = ["*.dcm"]

    def process(self, event):
        """removed"""

    def on_created(self, event):
        self.process(event)
        ds = pydicom.dcmread(event.src_path, force=True)
        info = fileReader.getInfo(ds, event.src_path)
        upload(info)


def enter():
    # путь до папки отслеживания
    path = ''

    observer = Observer()
    observer.schedule(CrtHandler(), path=path)
    observer.start()
    
    try:
        while True:
            time.sleep(10)
            
    except KeyboardInterrupt as e:
        print(e)
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    enter()