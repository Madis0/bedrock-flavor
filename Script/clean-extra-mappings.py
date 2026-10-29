# Removes lines from extra-mappings.csv that already exist in mappings.csv

from pathlib import Path

# File names
script_dir = Path(__file__).resolve().parent
mappings_file = script_dir / 'Extra' / 'mappings.csv'
extra_mappings_file = script_dir / 'Extra' / 'extra-mappings.csv'

def read_mappings(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return set(file.readlines())

def remove_duplicate_generic_mappings():
    mappings = read_mappings(mappings_file)
    with open(extra_mappings_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(extra_mappings_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if line not in mappings:
                file.write(line)

def main():
    remove_duplicate_generic_mappings()

if __name__ == "__main__":
    main()