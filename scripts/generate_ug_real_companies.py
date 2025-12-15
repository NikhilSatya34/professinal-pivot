import csv
import random

STREAM = "UG"

departments_roles = {
    "BSc": [
        ("Data Analyst", "Excel, SQL"),
        ("Lab Assistant", "Lab Techniques"),
        ("Research Assistant", "Data Collection"),
        ("Quality Analyst", "Basic QA"),
        ("Junior Scientist", "Scientific Methods")
    ],
    "BCA": [
        ("Junior Software Developer", "Python, Java"),
        ("Web Developer", "HTML, CSS, JS"),
        ("System Support Executive", "OS, Networking"),
        ("Database Assistant", "MySQL"),
        ("QA Tester", "Manual Testing")
    ],
    "BCom": [
        ("Accounts Executive", "Accounting, Tally"),
        ("Business Analyst", "Excel, Reporting"),
        ("Audit Assistant", "Auditing"),
        ("Finance Executive", "Finance Basics"),
        ("Operations Executive", "Business Ops")
    ],
    "BA": [
        ("Content Analyst", "Content Writing"),
        ("HR Executive", "Recruitment"),
        ("Marketing Executive", "Digital Marketing"),
        ("Operations Coordinator", "Operations"),
        ("Research Assistant", "Documentation")
    ]
}

locations = ["Hyderabad","Bengaluru","Chennai","Mumbai","Delhi","Pune"]

high_companies = [
    "Infosys","TCS","Wipro","Accenture","Cognizant",
    "IBM","Capgemini","HCL","Tech Mahindra","Amazon"
]

mid_companies = [
    "Zoho","Freshworks","LTIMindtree","Mphasis",
    "Hexaware","UST Global","Virtusa","Birlasoft"
]

startup_companies = [
    "Swiggy","Zomato","Meesho","Udaan","Groww",
    "CRED","Razorpay","PhonePe","Nykaa","Unacademy",
    "Byjus","Urban Company","PolicyBazaar","Licious","BigBasket"
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

with open("UG_520+.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "stream","department","job_role",
        "company_level","company_name",
        "location","required_skills"
    ])
    writer.writerows(rows)

print("✅ UG_520+.csv generated")
