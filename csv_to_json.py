import csv
import json
import sys

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(f"Converted {csv_file_path} to {json_file_path} successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py input.csv output.json")
    else:
        csv_file = sys.argv[1]
        json_file = sys.argv[2]
        csv_to_json(csv_file, json_file)