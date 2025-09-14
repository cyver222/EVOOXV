# EVOOX VX Ultimate

نسخة Ultimate من أداة EVOOX VX لفحص الملفات والروابط على Kali Linux.

## مميزات
- فحص ملفات (hashes, PE analysis, OCR, metadata)
- فحص روابط عبر VirusTotal
- تكامل مع VirusTotal API (مفتاح مضمن في core/api_integration.py)
- تقارير JSON
- فحص متعدد الخيوط

## تشغيل
1. ثبت المتطلبات (يفضل داخل virtualenv):
```bash
sudo apt update
sudo apt install tesseract-ocr -y
pip3 install -r requirements.txt
```

2. شغّل الأداة:
```bash
python3 evoox_vx2.py
```

## ملاحظات أمان
- لا تستخدم هذه الأداة بطرق غير قانونية.
- الـ API key مضمّن في المشروع؛ إن أردت تغييره فعدّل `core/api_integration.py`.
