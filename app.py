from flask import Flask, render_template, request

app = Flask(__name__)

# Skill database (you can add more later)
SKILLS_DB = [
    "Python", "Java", "C", "C++", "SQL",
    "Machine Learning", "Deep Learning", "Data Science",
    "Flask", "Django", "HTML", "CSS", "JavaScript",
    "React", "Node.js", "Git", "GitHub", "AWS", "Azure"
]

def extract_skills(resume_text):
    skills_found = []
    resume_lower = resume_text.lower()

    for skill in SKILLS_DB:
        if skill.lower() in resume_lower:
            skills_found.append(skill)

    return skills_found

def generate_summary(resume_text):
    lines = resume_text.split("\n")
    summary = " ".join(lines[:4])
    return summary

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    skills = []

    if request.method == "POST":
        resume_text = request.form.get("resume")
        summary = generate_summary(resume_text)
        skills = extract_skills(resume_text)

    return render_template(
        "index.html",
        summary=summary,
        skills=skills
    )

if __name__ == "__main__":
    app.run(debug=True)