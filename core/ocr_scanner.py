#!/usr/bin/env python3
from PIL import Image
import pytesseract
import PyPDF2
import docx
import os

def ocr_file(path):
    ext = os.path.splitext(path)[1].lower()
    text_output = ""
    try:
        if ext in [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]:
            text_output = pytesseract.image_to_string(Image.open(path))
        elif ext == ".pdf":
            try:
                reader = PyPDF2.PdfReader(path)
                for page in reader.pages:
                    text_output += page.extract_text() or ""
            except Exception:
                pass
        elif ext == ".docx":
            doc = docx.Document(path)
            for para in doc.paragraphs:
                text_output += para.text + "\\n"
        if text_output.strip():
            print("📝 نص مستخرج (أول 500 حرف):")
            print(text_output[:500])
        else:
            print("ℹ️ لا يوجد نص مستخرج.")
    except Exception as e:
        print("⚠️ خطأ في OCR:", e)
