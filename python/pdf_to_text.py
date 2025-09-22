import pdfplumber
import sys

pdf_path = sys.argv[1]   # PDF 
txt_path = sys.argv[2]   # TXT 

with pdfplumber.open(pdf_path) as pdf:
    lines = []
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            lines.extend(text.splitlines())

# Cleaning up unnecessary 
lines = [line.replace('\x0c','').strip() for line in lines if line.strip()]

with open(txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"{txt_path} has been created.")
