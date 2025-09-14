"""فحص الملفات شامل"""
import os, hashlib, json

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'virus_signatures.json')

def run(args):
    if not args:
        print("Usage: file_scanner <file_path>")
        return
    path = args[0]
    if not os.path.exists(path):
        print("الملف غير موجود:", path)
        return
    with open(DATA_FILE) as f:
        signatures = json.load(f)
    with open(path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h in signatures:
        print("⚠️ تم الكشف عن فيروس!")
    else:
        print("✅ الملف نظيف.")
