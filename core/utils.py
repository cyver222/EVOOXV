"""أدوات مساعدة: hash, logging, OCR"""
import hashlib

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
