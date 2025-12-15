import csv
import random

STREAM = "PG"

departments_roles = {
    "MSc": [
        ("Data Scientist", "Python, Statistics"),
        ("Research Scientist", "Research Methods"),
        ("ML Engineer", "Machine Learning"),
        ("Lab Scientist", "Advanced Lab Skills"),
        ("Analytics Consultant", "Data Analytics")
    ],
    "MCA": [
        ("Software Engineer", "Java, Python"),
        ("Backend Developer", "Spring Boot"),
        ("Cloud Engineer", "AWS, Azure"),
        ("DevOps Engineer", "Docker, CI/CD"),
        ("System Architect", "System Design")
    ],
    "MBA": [
        ("Business Analyst", "Business Analysis"),
        ("Product Manager", "Product Strategy"),
        ("HR Manager", "Human Resources"),
        ("Marketing Manager", "Marketing Strategy"),
        ("Operations Manager", "Operations")
    ],
    "MTech": [
        ("R&D Engineer", "Advanced Engineering"),
        ("Project Engineer", "Technical Projects"),
        ("Systems Engineer", "System Engineering"),
        ("Automation Engineer", "Automation Tools"),
        ("Design Specialist", "Advanced Design")
    ]
}

locations = ["Bengaluru","Hyderabad","Pune","Mumbai","Chennai","Gurgaon"]

high_companies = [
    "Google","Microsoft","Amazon","IBM","Oracle",
    "Infosys","Accenture","Qualcomm","Intel","Siemens"
]

mid_companies = [
    "Zoho","Freshworks","LTIMindtree","Persistent",
    "KPIT","Cyient","Ramco Systems","Happiest Minds"
]

startup_companies = [
    "Razorpay","Groww","Zerodha","CRED","Slice",
    "Jupiter","Navi","BrowserStack","Postman",
    "Chargebee","Innovaccer","Fractal Analytics"
]

rows = []

def generate(companies, level, count):
    for _ in range(count):
        dept = random.choice(list(departments_roles.keys()))
        role, skills = random.choice(departments_roles[dept])
        rows.append([
            STREAM,
            dept,
            role,
            level,
            random.choice(companies),
            random.choice(locations),
            skills
        ])

generate(startup_companies, "Startup", 300)
generate(mid_companies, "Mid", 150)
generate(high_companies, "High", 70)

with open("PG_520+.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "stream","department","job_role",
        "company_level","company_name",
        "location","required_skills"
    ])
    writer.writerows(rows)

print("✅ PG_520+.csv generated")
