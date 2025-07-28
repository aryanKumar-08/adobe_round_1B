import fitz
import json
import os
from relevance import rank_sections
from datetime import datetime

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()
        if text:
            for line in text.split("\n"):
                if len(line.strip()) > 5:
                    sections.append({"document": os.path.basename(pdf_path),
                                     "page": page_num,
                                     "text": line.strip()})
    return sections

if __name__ == "__main__":
    input_dir = "/app/input"
    output_dir = "/app/output"

    persona_path = os.path.join(input_dir, "persona.json")
    with open(persona_path, "r", encoding="utf-8") as f:
        persona_data = json.load(f)

    all_sections = []
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            all_sections.extend(extract_sections(pdf_path))

    ranked = rank_sections(all_sections, persona_data["persona"], persona_data["job"])

    output = {
        "metadata": {
            "documents": [f for f in os.listdir(input_dir) if f.endswith(".pdf")],
            "persona": persona_data["persona"],
            "job": persona_data["job"],
            "timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": ranked[:5],
        "sub_section_analysis": ranked[:5]
    }

    out_file = os.path.join(output_dir, "result.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
