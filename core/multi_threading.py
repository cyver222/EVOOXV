"""تشغيل عمليات متعددة الخيوط"""
import threading, time

def worker(name):
    print(f"Thread {name} يعمل...")
    time.sleep(2)
    print(f"Thread {name} انتهى.")

def run(args):
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"T{i+1}",))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("✅ كل الخيوط انتهت.")
