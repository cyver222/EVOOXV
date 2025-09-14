#!/usr/bin/env python3
import os
from colorama import Fore, Style
from core.file_scanner import scan_file, scan_multiple_files
from core.url_scanner import scan_url, scan_multiple_urls
from core.report import show_report
from core.utils import choose_language, update_virus_db, load_virus_db

lang = choose_language()

def banner():
    print(Fore.CYAN + """
 ████████╗██╗   ██╗██╗ ██████╗ ██████╗ ██╗  ██╗
 ╚══██╔══╝██║   ██║██║██╔═══██╗██╔══██╗██║ ██╔╝
    ██║   ██║   ██║██║██║   ██║██████╔╝█████╔╝ 
    ██║   ██║   ██║██║██║   ██║██╔═══╝ ██╔═██╗ 
    ██║   ╚██████╔╝██║╚██████╔╝██║     ██║  ██╗
    ╚═╝    ╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝
""" + Style.RESET_ALL)

def main_menu():
    while True:
        print("\n1.", "فحص ملف" if lang=="ar" else "Scan File")
        print("2.", "فحص رابط" if lang=="ar" else "Scan URL")
        print("3.", "تكامل API" if lang=="ar" else "API Integration")
        print("4.", "توليد تقرير" if lang=="ar" else "Show Report")
        print("5.", "تشغيل متعدد الخيوط" if lang=="ar" else "Multi-thread Scan")
        print("6.", "تحليل Metadata" if lang=="ar" else "Metadata Analysis")
        print("7.", "OCR للصور والملفات" if lang=="ar" else "OCR Files")
        print("8.", "تحديث قاعدة البيانات" if lang=="ar" else "Update Virus DB")
        print("0.", "خروج" if lang=="ar" else "Exit")
        choice = input(">>> ")

        if choice == "1":
            path = input("ادخل مسار الملف: " if lang=="ar" else "Enter file path: ")
            scan_file(path)
        elif choice == "2":
            url = input("ادخل الرابط: " if lang=="ar" else "Enter URL: ")
            scan_url(url)
        elif choice == "3":
            print("⚡ " + ("فحص API موجود" if lang=="ar" else "API integration is active"))
            # show keys status
            from core.api_integration import VT_API_KEY
            print("VirusTotal API key:", ("***hidden***" if VT_API_KEY else "Not set"))
        elif choice == "4":
            show_report()
        elif choice == "5":
            sub = input("1) " + ("ملفات" if lang=="ar" else "files") + " 2) " + ("روابط" if lang=="ar" else "urls") + "\n>>> ")
            if sub.strip() == "1":
                paths = input(("أدخل مسارات الملفات مفصولة بمسافة: " if lang=="ar" else "Enter file paths separated by space: "))
                lst = paths.split()
                scan_multiple_files(lst)
            else:
                urls = input(("أدخل الروابط مفصولة بمسافة: " if lang=="ar" else "Enter URLs separated by space: "))
                lst = urls.split()
                scan_multiple_urls(lst)
        elif choice == "6":
            path = input("ادخل مسار الملف: " if lang=="ar" else "Enter file path: ")
            from core.metadata_analysis import analyze_file_metadata
            analyze_file_metadata(path)
        elif choice == "7":
            path = input("ادخل مسار الملف: " if lang=="ar" else "Enter file path: ")
            from core.ocr_scanner import ocr_file
            ocr_file(path)
        elif choice == "8":
            print("🔄 " + ("جارٍ التحديث..." if lang=="ar" else "Updating..."))
            # example: add entry by user
            h = input("ادخل SHA256=label (مثال: abc..=TestMal) : ")
            if "=" in h:
                k,v = h.split("=",1)
                update_virus_db({k.strip(): v.strip()})
            else:
                print("تنسيق خاطئ.")
        elif choice == "0":
            print("خروج..." if lang=="ar" else "Exiting...")
            break
        else:
            print("خيار غير صالح!" if lang=="ar" else "Invalid option!")

if __name__ == "__main__":
    banner()
    main_menu()
