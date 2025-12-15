import csv
import random

# ---------------- BASIC CONFIG ----------------
STREAM = "Engineering"

departments_roles = {
    "CSE": [
        ("Software Engineer", "Python, Java, DSA, OOP"),
        ("Backend Developer", "Java, Spring Boot, APIs"),
        ("Full Stack Developer", "HTML, CSS, JavaScript, React"),
        ("Data Analyst", "Python, SQL, Excel, Power BI"),
        ("Data Scientist", "Python, ML, Pandas, NumPy"),
        ("ML Engineer", "Python, TensorFlow, Scikit-learn"),
        ("DevOps Engineer", "Docker, Kubernetes, CI/CD"),
        ("Cloud Engineer", "AWS, Azure, Linux")
    ],
    "AI&DS": [
        ("Data Scientist", "Python, ML, Pandas"),
        ("ML Engineer", "TensorFlow, PyTorch"),
        ("AI Engineer", "Deep Learning, NLP"),
        ("Data Analyst", "SQL, Python"),
        ("Big Data Engineer", "Spark, Hadoop")
    ],
    "ECE": [
        ("Embedded Engineer", "C, Embedded Systems"),
        ("VLSI Engineer", "VHDL, Verilog"),
        ("IoT Engineer", "Sensors, MQTT"),
        ("Network Engineer", "Networking, Routing"),
        ("Signal Processing Engineer", "MATLAB, DSP")
    ],
    "EEE": [
        ("Electrical Design Engineer", "AutoCAD, Power Systems"),
        ("Power Systems Engineer", "Power Generation"),
        ("Control Systems Engineer", "PLC, SCADA"),
        ("Maintenance Engineer", "Electrical Maintenance"),
        ("Energy Analyst", "Renewable Energy")
    ],
    "Mechanical": [
        ("Design Engineer", "AutoCAD, SolidWorks"),
        ("Production Engineer", "Manufacturing Processes"),
        ("Quality Engineer", "Six Sigma"),
        ("Maintenance Engineer", "Plant Maintenance"),
        ("CAD Engineer", "CATIA, NX")
    ],
    "Civil": [
        ("Site Engineer", "AutoCAD, Site Management"),
        ("Planning Engineer", "MS Project, Primavera"),
        ("Structural Engineer", "ETABS, STAAD"),
        ("Quantity Surveyor", "Estimation, Billing"),
        ("Safety Engineer", "Construction Safety")
    ]
}

locations = [
    "Bengaluru", "Hyderabad", "Chennai", "Pune",
    "Mumbai", "Noida", "Gurgaon", "Coimbatore",
    "Kolkata", "Ahmedabad"
]

# ---------------- REAL COMPANY POOLS ----------------
high_companies = [
    "TCS","Infosys","Wipro","Accenture","Cognizant","IBM",
    "Capgemini","HCL","Tech Mahindra","Oracle","Google",
    "Microsoft","Amazon","Qualcomm","Bosch","Siemens",
    "L&T","Tata Projects","Intel","Honeywell"
]

mid_companies = [
    "Zoho","Freshworks","LTIMindtree","Mphasis","Hexaware",
    "UST Global","Virtusa","KPIT","Cyient","Sonata Software",
    "Persistent Systems","Newgen","Birlasoft","Tata Elxsi",
    "Ramco Systems","Sasken","Happiest Minds","Innominds",
    "ValueLabs","Rapid7","Infogain","Coforge"
]

startup_companies = [
    "Razorpay","PhonePe","Paytm","CRED","Zerodha","Groww",
    "Swiggy","Zomato","Meesho","Udaan","InMobi","BrowserStack",
    "Postman","Chargebee","Innovaccer","Practo","Ninjacart",
    "Ather Energy","Ola Electric","Delhivery","Dunzo","Porter",
    "BigBasket","Nykaa","Byjus","Unacademy","Vedantu",
    "PhysicsWallah","Fractal Analytics","Tiger Analytics",
    "Mu Sigma","Tredence","Quantiphi","GreyOrange",
    "OfBusiness","InfraMarket","Zetwerk","Slice","Jupiter",
    "Navi","CARS24","Spinny","Urban Company","PolicyBazaar",
    "ACKO","Digit Insurance"
]

# ---------------- ROW GENERATION ----------------
rows = []

def generate_rows(companies, level, target_count):
    count = 0
    while count < target_count:
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
generate_rows(startup_companies, "Startup", 550)
generate_rows(mid_companies, "Mid", 250)
generate_rows(high_companies, "High", 120)

# ---------------- WRITE CSV ----------------
with open("Engineering_900+.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "stream",
        "department",
        "job_role",
        "company_level",
        "company_name",
        "location",
        "required_skills"
    ])
    writer.writerows(rows)

print("✅ Engineering_900+.csv generated with REAL companies (900+ rows)")
