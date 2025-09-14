#!/usr/bin/env python3
import requests, os, base64, time, json

# Put your VirusTotal API key here. Provided earlier by user.
VT_API_KEY = "a8c1333e39846820f8effaa2a0d0cbec80d8a2a44ff66e89d1bc1064cb5fa9f8"

HEADERS = {"x-apikey": VT_API_KEY}

def virustotal_file_scan(file_path, wait_for_result=True, poll_interval=2, max_tries=15):
    """
    Upload file to VirusTotal, optionally poll for analysis result.
    Returns dict with minimal results or None on failure.
    """
    try:
        url = "https://www.virustotal.com/api/v3/files"
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            r = requests.post(url, headers=HEADERS, files=files)
        if r.status_code in (200,202):
            resp = r.json()
            analysis_id = resp.get("data",{}).get("id")
            if not wait_for_result:
                return {"analysis_id": analysis_id}
            # poll analysis
            for i in range(max_tries):
                time.sleep(poll_interval)
                r2 = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=HEADERS)
                if r2.status_code == 200:
                    j = r2.json()
                    status = j.get("data",{}).get("attributes",{}).get("status")
                    if status == "completed":
                        stats = j.get("data",{}).get("attributes",{}).get("stats",{})
                        malicious = stats.get("malicious",0)
                        return {"analysis_id": analysis_id, "malicious_count": malicious, "stats": stats}
            return {"analysis_id": analysis_id}
        else:
            print("⚠️ فشل في رفع الملف لـ VirusTotal:", r.status_code, r.text[:200])
            return None
    except Exception as e:
        print("⚠️ خطأ في التواصل مع VirusTotal:", e)
        return None

def virustotal_file_analysis(analysis_id):
    try:
        r = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=HEADERS)
        if r.status_code == 200:
            j = r.json()
            stats = j.get("data",{}).get("attributes",{}).get("stats",{})
            return stats
    except:
        pass
    return None

def virustotal_scan(url):
    """Check URL via VirusTotal. Returns dict with malicious_count."""
    try:
        encoded = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        r = requests.get(f"https://www.virustotal.com/api/v3/urls/{encoded}", headers=HEADERS)
        if r.status_code == 200:
            j = r.json()
            attrs = j.get("data",{}).get("attributes",{})
            last = attrs.get("last_analysis_stats", {})
            malicious = last.get("malicious", 0) or last.get("malicious", 0)
            return {"malicious_count": malicious, "stats": last}
        elif r.status_code == 404:
            # not found — submit for scanning
            submit = requests.post("https://www.virustotal.com/api/v3/urls", headers=HEADERS, data={"url": url})
            if submit.status_code in (200,201,202):
                rid = submit.json().get("data",{}).get("id")
                # try to fetch analysis (best effort)
                time.sleep(2)
                return {"submitted_id": rid}
        else:
            print("⚠️ خطأ من VirusTotal:", r.status_code)
    except Exception as e:
        print("⚠️ خطأ عند طلب VirusTotal:", e)
    return None
