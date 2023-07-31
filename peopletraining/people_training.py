import csv
from datetime import datetime

try:
    with open("PeopleTrainingDate.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        sorted_rows = sorted(rows, key=lambda row: datetime.strptime(row['Updated'], '%d/%m/%Y'))
        
        for row in sorted_rows:
            for key, value in row.items():
                print(f"{key}: {value}")
            print()

except FileNotFoundError:
    print("File not found!")
    
except Exception as e:
    print(f"An error occurred: {e}")
