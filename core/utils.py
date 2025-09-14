#!/usr/bin/env python3
import json, os, hashlib
from datetime import datetime

VIRUS_DB_FILE = "data/virus_signatures.json"
REPORT_FILE = "data/report.json"

def choose_language():
    lang = input("اختر اللغة: 1=عربي, 2=English: ")
    return "ar" if lang.strip()=="1" else "en"

def compute_hashes(path):
    try:
        with open(path,"rb") as f:
            data = f.read()
        return {
            "md5": hashlib.md5(data).hexdigest(),
            "sha1": hashlib.sha1(data).hexdigest(),
            "sha256": hashlib.sha256(data).hexdigest(),
            "sha512": hashlib.sha512(data).hexdigest()
        }
    except Exception as e:
        print("⚠️ خطأ في حساب الهاش:", e)
        return None

def load_virus_db():
    try:
        with open(VIRUS_DB_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def log_scan(path, hashes):
    entry = {
        "type": "file",
        "path": path,
        "hashes": hashes,
        "time": datetime.utcnow().isoformat()+"Z"
    }
    data = []
    if os.path.exists(REPORT_FILE):
        try:
            with open(REPORT_FILE,"r",encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []
    data.append(entry)
    with open(REPORT_FILE,"w",encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def log_scan_url(url):
    entry = {"type":"url","url":url,"time": datetime.utcnow().isoformat()+"Z"}
    data = []
    if os.path.exists(REPORT_FILE):
        try:
            with open(REPORT_FILE,"r",encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []
    data.append(entry)
    with open(REPORT_FILE,"w",encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def update_virus_db(new_entries):
    db = {}
    if os.path.exists(VIRUS_DB_FILE):
        try:
            with open(VIRUS_DB_FILE,"r",encoding="utf-8") as f:
                db = json.load(f)
        except:
            db = {}
    db.update(new_entries)
    with open(VIRUS_DB_FILE,"w",encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
    print("✅ قاعدة البيانات تم تحديثها!")
