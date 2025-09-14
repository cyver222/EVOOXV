"""فحص شامل للروابط"""
import sys

def run(args):
    if not args:
        print("Usage: url_scanner <url>")
        return
    url = args[0]
    print(f"فحص الرابط: {url}")
