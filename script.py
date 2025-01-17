import json
import sys

def compare_and_update_json(old_file_path, new_file_path, output_file_path):
    # Load the old JSON file
    with open(old_file_path, 'r') as old_file:
        old_data = json.load(old_file)

    # Load the new JSON file
    with open(new_file_path, 'r') as new_file:
        new_data = json.load(new_file)

    # List to store updated data
    updated_data = []

    # Compare old and new JSON objects
    for old_item in old_data:
        matched = False
        for new_item in new_data:
            if old_item["Old_Page"] == new_item["Old_Page"] and old_item["New_Page"] == new_item["New_Page"]:
                old_item["Redirection"] = 301  # Update redirection to 301
                matched = True
                break
        updated_data.append(old_item)

    # Save the updated JSON data to a new file
    with open(output_file_path, 'w') as output_file:
        json.dump(updated_data, output_file, indent=4)

    print(f"Updated JSON saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <old_file_path> <new_file_path> <output_file_path>")
        sys.exit(1)

    old_file_path = sys.argv[1]
    new_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    compare_and_update_json(old_file_path, new_file_path, output_file_path)
