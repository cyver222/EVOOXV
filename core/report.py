#!/usr/bin/env python3
import json, os
REPORT_FILE = "data/report.json"

def show_report():
    if not os.path.exists(REPORT_FILE):
        print("لا توجد تقارير بعد.")
        return
    with open(REPORT_FILE,"r",encoding="utf-8") as f:
        data = json.load(f)
        for i,entry in enumerate(data,1):
            print(f"--- Report #{i} ---")
            print(json.dumps(entry, indent=4, ensure_ascii=False))
