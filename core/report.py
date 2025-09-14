"""توليد وعرض تقارير"""
import json, os
from datetime import datetime

REPORT_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'report.json')

def run(args):
    now = datetime.utcnow().isoformat()
    report_data = {"generated_at": now, "summary": "نتائج الفحص هنا"}
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4)
    print("✅ تم توليد التقرير في:", REPORT_FILE)
