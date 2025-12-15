import csv

input_files = [
    "Engineering_900+.csv",
    "Medical_450+.csv",
    "Pharmacy_210+.csv",
    "UG_520+.csv",
    "PG_520+.csv"
]

output_file = "Master_companies_list.csv"

all_rows = []
header = None

for file in input_files:
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        file_header = next(reader)

        if header is None:
            header = file_header  # take header from first file
            all_rows.append(header)

        for row in reader:
            all_rows.append(row)

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(all_rows)

print(f"✅ {output_file} created successfully!")
print(f"📊 Total rows (including header): {len(all_rows)}")
