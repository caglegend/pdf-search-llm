import pdfplumber
import sys

pdf_path = sys.argv[1]   # PDF yolu
txt_path = sys.argv[2]   # TXT yolu

with pdfplumber.open(pdf_path) as pdf:
    lines = []
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            lines.extend(text.splitlines())

# Gereksiz karakterleri temizle
lines = [line.replace('\x0c','').strip() for line in lines if line.strip()]

with open(txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"{txt_path} oluşturuldu.")
