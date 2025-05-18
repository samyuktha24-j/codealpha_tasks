import csv

# Check if the new data already exists in the database
def is_duplicate(new_data, filename='database.csv'):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Email'] == new_data['Email']:
                return True
    return False

# Add new data if it's not a duplicate
def add_data(new_data, filename='database.csv'):
    if not is_duplicate(new_data, filename):
        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Email"])
            writer.writerow(new_data)
        print("Data added successfully.")
    else:
        print("Duplicate found. Data not added.")

# ✅ Test Example
new_entry = {"Name": "Theiya", "Email": "theiya@example.com"}
add_data(new_entry)
