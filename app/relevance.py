def rank_sections(sections, persona, job):
    keywords = set((persona + " " + job).lower().split())
    ranked = []
    for sec in sections:
        score = sum(1 for word in keywords if word in sec["text"].lower())
        sec_out = {
            "document": sec["document"],
            "page": sec["page"],
            "section_title": sec["text"][:50],
            "importance_rank": score,
            "refined_text": sec["text"]
        }
        ranked.append(sec_out)
    ranked.sort(key=lambda x: x["importance_rank"], reverse=True)
    return ranked
