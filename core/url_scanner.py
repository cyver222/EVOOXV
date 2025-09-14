#!/usr/bin/env python3
import requests
from core.api_integration import virustotal_scan
from core.utils import log_scan_url
from core.multi_threading import run_in_threads

def scan_url(url):
    url = url.strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        r = requests.get(url, timeout=8, allow_redirects=True)
        status = r.status_code
        print(f"URL: {url} | HTTP {status}")
        vt = virustotal_scan(url)
        if vt and vt.get("malicious_count",0) > 0:
            print(f"⚠️ الرابط مشبوه حسب VirusTotal ({vt.get('malicious_count')} detections)")
        else:
            print("✅ الرابط يبدو نظيفا (حسب الفحص السريع)")
    except Exception as e:
        print("⚠️ خطأ في الوصول:", e)
    log_scan_url(url)
    return

def scan_multiple_urls(list_urls):
    run_in_threads(scan_url, list_urls)
