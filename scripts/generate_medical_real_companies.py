import csv
import random

STREAM = "Medical"

departments_roles = {
    "General Medicine": [
        ("Clinical Analyst", "Clinical Data Analysis, EHR"),
        ("Medical Officer", "Patient Care, Diagnosis"),
        ("Healthcare Consultant", "Hospital Operations"),
        ("Clinical Research Associate", "Clinical Trials"),
        ("Public Health Analyst", "Epidemiology, Statistics")
    ],
    "Nursing": [
        ("Staff Nurse", "Patient Care, Monitoring"),
        ("Clinical Nurse", "Clinical Procedures"),
        ("ICU Nurse", "Critical Care"),
        ("Nurse Educator", "Medical Training"),
        ("Care Coordinator", "Patient Management")
    ],
    "Medical Lab Technology": [
        ("Lab Technician", "Pathology, Lab Testing"),
        ("Medical Lab Technologist", "Biochemistry, Hematology"),
        ("Quality Control Analyst", "Lab Quality Standards"),
        ("Lab Supervisor", "Lab Operations"),
        ("Diagnostic Analyst", "Medical Diagnostics")
    ],
    "Radiology": [
        ("Radiology Technologist", "X-Ray, CT, MRI"),
        ("Imaging Specialist", "Medical Imaging"),
        ("Radiology Analyst", "Image Analysis"),
        ("CT Scan Technician", "CT Equipment"),
        ("MRI Technician", "MRI Operations")
    ],
    "Healthcare Management": [
        ("Hospital Administrator", "Hospital Operations"),
        ("Healthcare Manager", "Healthcare Management"),
        ("Medical Operations Analyst", "Process Optimization"),
        ("Health Information Manager", "Medical Records"),
        ("Quality Manager", "Healthcare Quality")
    ],
    "Biomedical": [
        ("Biomedical Engineer", "Medical Devices"),
        ("Clinical Engineer", "Equipment Maintenance"),
        ("Medical Device Analyst", "Device Testing"),
        ("Regulatory Affairs Executive", "Medical Regulations"),
        ("Service Engineer", "Medical Equipment Service")
    ]
}

locations = [
    "Hyderabad", "Bengaluru", "Chennai", "Mumbai",
    "Delhi", "Pune", "Kolkata", "Ahmedabad"
]

high_companies = [
    "Apollo Hospitals","Fortis Healthcare","Manipal Hospitals",
    "Max Healthcare","AIIMS","Narayana Health","Medanta",
    "Siemens Healthineers","GE Healthcare","Philips Healthcare"
]

mid_companies = [
    "Dr Lal PathLabs","Metropolis Healthcare","Thyrocare",
    "SRL Diagnostics","Aster DM Healthcare","Care Hospitals",
    "Rainbow Hospitals","KIMS Hospitals","Vijaya Diagnostics",
    "Oncquest Labs"
]

startup_companies = [
    "Practo","PharmEasy","Tata 1mg","Portea Medical",
    "HealthifyMe","MFine","DocsApp","NetMeds","CureFit",
    "Qure.ai","Niramai","SigTuple","Dozee","Innovaccer Health",
    "Tricog Health","MedGenome"
]

rows = []

def generate_rows(companies, level, target):
    count = 0
    while count < target:
        company = random.choice(companies)
        dept = random.choice(list(departments_roles.keys()))
        role, skills = random.choice(departments_roles[dept])
        location = random.choice(locations)

        rows.append([
            STREAM,
            dept,
            role,
            level,
            company,
            location,
            skills
        ])
        count += 1

# REQUIRED COUNTS
generate_rows(startup_companies, "Startup", 250)
generate_rows(mid_companies, "Mid", 150)
generate_rows(high_companies, "High", 50)

with open("Medical_450+.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "stream","department","job_role",
        "company_level","company_name",
        "location","required_skills"
    ])
    writer.writerows(rows)

print("✅ Medical_450+.csv generated with REAL companies")
