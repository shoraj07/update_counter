import os
import json

# Load the JSON data from the file
json_file_path = 'Json_counter/counter_json.json'  # Replace with the path to your JSON file
with open(json_file_path, 'r') as f:
    data = json.load(f)

def update_count(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]
            if txt_files:
                parts = dir_path.replace(directory_path, '').strip(os.sep).split(os.sep)
                if len(parts) < 4:
                    continue
                first_element, second_element, seventh_element, forth_element = [part.lower() for part in parts[:4]]
                
                # Check if there's a matching entry in the JSON (case insensitive)
                matched_entry = None
                for entry in data:
                    if (entry['first_element'].lower() == first_element and
                        entry['second_element'].lower() == second_element and
                        entry['seventh_element'].lower() == seventh_element and
                        entry['forth_element'].lower() == forth_element):
                        matched_entry = entry
                        break
                
                if matched_entry:
                    matched_entry['count'] += 1
                else:
                    new_entry = {
                        'first_element': first_element,
                        'second_element': second_element,
                        'seventh_element': seventh_element,
                        'forth_element': forth_element,
                        'count': 1
                    }
                    data.append(new_entry)

# Directory path where the directories are located
base_directory_path = 'destFolders'  # Replace with the path to your base directory

# Update the counts based on the directory contents
update_count(base_directory_path)

# Save the updated JSON data back to the file
with open(json_file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("JSON file updated successfully.")
