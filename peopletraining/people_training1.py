
import csv
from datetime import datetime

destination_fieldnames = ['Title', 'Name', 'ID', 'Email', 'Company', 'Updated']

# Read the existing data
try:
    with open('PeopleTrainingData .csv', 'r') as file:
        reader = csv.DictReader(file)
        existing_rows = list(reader)

    # Open the update file
    with open('PeopleTrainingDataUpdate.csv', 'r') as file:
        reader = csv.DictReader(file)
        update_rows = list(reader)

        # Reorder the columns of the update rows
        reordered_update_rows = [{fieldname: row.get(fieldname, '') for fieldname in destination_fieldnames} for row in update_rows]

        # Append the reordered update rows to the existing data
        existing_rows.extend(reordered_update_rows)

    # Sort all the rows by the "Updated" date
    sorted_rows = sorted(existing_rows, key=lambda row: datetime.strptime(row['Updated'], '%d/%m/%Y'))

    # Write the sorted rows back to the original file
    with open('PeopleTrainingData.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=destination_fieldnames)
        writer.writeheader() # Write the header
        writer.writerows(sorted_rows) # Write the sorted rows

    print("File updated and sorted successfully!")

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print(f"An error occurred: {e}")
