#!/usr/bin/env python3
import pefile

def analyze_exe(path):
    try:
        pe = pefile.PE(path)
        suspicious = []
        # suspicious if many sections or strange entrypoint
        for s in pe.sections:
            name = s.Name.decode(errors="ignore").strip("\\x00")
            if name.lower() in ("rsrc","reloc",".ndata"):
                continue
            if s.SizeOfRawData == 0 or s.Misc_VirtualSize == 0:
                suspicious.append(name)
        # check imports
        try:
            imports = [imp.name.decode() for entry in pe.DIRECTORY_ENTRY_IMPORT for imp in entry.imports if imp.name]
        except Exception:
            imports = []
        if len(suspicious) > 0 or len(imports) < 3:
            return f"⚠️ نتيجة تحليل PE: أقسام مشبوهة: {suspicious} | imports_count={len(imports)}"
    except Exception as e:
        return None
    return None
