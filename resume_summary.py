def generate_summary(text):
    lines = text.split("\n")
    summary = " ".join(lines[:5])
    return summary