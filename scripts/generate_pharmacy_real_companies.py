import csv
import random

STREAM = "Pharmacy"

departments_roles = {
    "Pharmaceutics": [
        ("Formulation Scientist", "Drug Formulation, GMP"),
        ("Production Executive", "Manufacturing, SOP"),
        ("Quality Assurance Officer", "QA, Documentation"),
        ("Validation Executive", "Process Validation"),
        ("Research Associate", "Pharmaceutical Research")
    ],
    "Pharmacology": [
        ("Clinical Research Associate", "Clinical Trials"),
        ("Drug Safety Associate", "Pharmacovigilance"),
        ("Medical Writer", "Clinical Documentation"),
        ("Regulatory Affairs Executive", "Drug Regulations"),
        ("Pharmacovigilance Analyst", "Adverse Event Reporting")
    ],
    "Pharmaceutical Analysis": [
        ("QC Analyst", "HPLC, GC"),
        ("Analytical Chemist", "Method Validation"),
        ("Quality Control Officer", "Lab QA"),
        ("Stability Analyst", "Stability Studies"),
        ("Calibration Executive", "Instrument Calibration")
    ]
}

locations = ["Hyderabad","Bengaluru","Mumbai","Chennai","Pune","Ahmedabad"]

high_companies = [
    "Sun Pharma","Dr Reddy's","Cipla","Aurobindo Pharma",
    "Lupin","Pfizer","Novartis","GSK","Abbott","Sanofi"
]

mid_companies = [
    "Alkem Laboratories","Torrent Pharma","Glenmark",
    "Biocon","IPCA Laboratories","Natco Pharma",
    "Zydus Lifesciences","Alembic Pharma"
]

startup_companies = [
    "PharmEasy","Tata 1mg","NetMeds","Medlife",
    "HealthKart","Wellness Forever","Truemeds",
    "Plix","Bold Care","Himalayan Organics"
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

generate(startup_companies, "Startup", 100)
generate(mid_companies, "Mid", 80)
generate(high_companies, "High", 30)

with open("Pharmacy_210+.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "stream","department","job_role",
        "company_level","company_name",
        "location","required_skills"
    ])
    writer.writerows(rows)

print("✅ Pharmacy_210+.csv generated")
