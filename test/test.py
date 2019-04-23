from flask import Flask, current_app

import threading
import time
from werkzeug.local import Local

t = threading.current_thread()
print(t.getName())

class A:
    t = 1

l = Local()
l.b = 1

def worker():
    t = threading.current_thread()
    # print(t.getName())
    l.b = 2
    time.sleep(7)
    print('hello')


t1 = threading.Thread(target=worker, daemon=True)
t1.start()
print(l.b)
# t1.join()

