#!/usr/bin/env python3
import os
from core.utils import compute_hashes, load_virus_db, log_scan
from core.api_integration import virustotal_file_scan, virustotal_file_analysis
from core.metadata_analysis import analyze_file_metadata
from core.ocr_scanner import ocr_file
from core.pe_analyzer import analyze_exe
from core.multi_threading import run_in_threads

def scan_file(path):
    path = path.strip()
    if not os.path.exists(path):
        print("⚠️ الملف غير موجود!")
        return
    hashes = compute_hashes(path)
    if not hashes:
        return
    virus_db = load_virus_db()
    local_result = virus_db.get(hashes.get("sha256"))
    # Basic output
    print(f"File: {path}")
    print(f"MD5: {hashes.get('md5')}")
    print(f"SHA256: {hashes.get('sha256')}")
    # Metadata and OCR
    analyze_file_metadata(path)
    ocr_file(path)
    # PE analysis if exe
    exe_result = None
    if path.lower().endswith(('.exe','.dll','.bin')):
        exe_result = analyze_exe(path)
        if exe_result:
            print(exe_result)
    # Send to VirusTotal and wait for result (non-blocking prints inside)
    vt_result = virustotal_file_scan(path)
    # Log scan locally
    log_scan(path, hashes)
    # Decide final message
    if local_result:
        print(f"⚠️ الملف مصاب (قاعدة البيانات): {local_result}")
    elif vt_result and vt_result.get("malicious_count",0) > 0:
        print(f"⚠️ الملف مصاب حسب VirusTotal ({vt_result.get('malicious_count')} detections)")
    elif exe_result:
        print("⚠️ الملف مشبوه بحسب تحليل PE")
    else:
        print("✅ الملف نظيف (لا توجد دلائل محلية على الإصابة)")
    return

def scan_multiple_files(list_paths):
    run_in_threads(scan_file, list_paths)
