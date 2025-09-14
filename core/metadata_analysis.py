#!/usr/bin/env python3
import magic, os

def analyze_file_metadata(path):
    try:
        file_type = magic.from_file(path)
    except Exception:
        file_type = "Unknown"
    try:
        size = os.path.getsize(path)
    except Exception:
        size = 0
    print(f"📄 نوع الملف: {file_type} | حجم الملف: {size} bytes")
