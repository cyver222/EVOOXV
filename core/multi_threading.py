#!/usr/bin/env python3
import threading

def run_in_threads(function, items):
    threads = []
    for item in items:
        t = threading.Thread(target=function, args=(item,))
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
