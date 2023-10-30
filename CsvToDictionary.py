import csv

def read_csv_to_dictionary(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the CSV has a unique identifier field named 'id'
            # You can change it to the appropriate column name in your CSV
            data[row['student_id']] = row
    return data


csv_file_path = "C:\\Users\\Amirhoseyn\\Downloads\\MOCK_DATA.csv"
csv_data = read_csv_to_dictionary(csv_file_path)
print(csv_data)