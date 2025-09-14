#!/usr/bin/env python3
"""EVOOX VX2 - CLI رئيسي مع بانر وقائمة"""
import sys
from core import file_scanner, url_scanner, api_integration, report, utils
from core import multi_threading, metadata_analysis, ocr_scanner

BANNER = r'''
 ______  __     ___   ___   ___   __
|  ____| \ \   / / | | | | | | | |
| |__     \ \_/ /  | | | | | | | |
|  __|     \   /   | | | | | | | |
| |____     | |    | |_| | | |_| |
|______|    |_|     \___/   \___/
EVOOX VX2 - Advanced File & URL Scanner
'''

MENU = """القائمة:
1) فحص ملف
2) فحص رابط
3) تكامل API
4) توليد تقرير
5) تشغيل متعدد الخيوط
6) تحليل Metadata
7) OCR للصور والملفات
0) خروج
"""

def main():
    print(BANNER)
    while True:
        print(MENU)
        choice = input("EVOOX> ").strip()
        if choice in ("0", "exit", "quit"):
            print("وداعاً!")
            break
        handle_choice(choice)

def handle_choice(choice):
    try:
        if choice == "1":
            path = input("أدخل مسار الملف: ")
            file_scanner.run([path])
        elif choice == "2":
            url = input("أدخل الرابط: ")
            url_scanner.run([url])
        elif choice == "3":
            api_integration.run([])
        elif choice == "4":
            report.run([])
        elif choice == "5":
            multi_threading.run([])
        elif choice == "6":
            metadata_analysis.run([])
        elif choice == "7":
            ocr_scanner.run([])
        else:
            print("خيار غير معروف")
    except Exception as e:
        print("خطأ:", e)

if __name__ == "__main__":
    main()
