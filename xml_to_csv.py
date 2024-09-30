import csv
import xml.etree.ElementTree as ET
import sys
import pathlib

def xml_to_csv(file_path, csv_name) -> None:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        sys.exit(f"Error parsing XML file: {e}")

    with open(csv_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        headers = get_headers(root)
        writer.writerow(headers)
        for record in root:
            row = get_row(record, headers)
            writer.writerow(row)

def get_headers(root):
    headers = set()
    for elem in root.iter():
        headers.update(child.tag for child in elem)
    return list(headers)

def get_row(record, headers):
    row = []
    for header in headers:
        element = record.find(header)
        row.append(element.text if element is not None else '')
    return row

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Two arguments required: one XML path and one save file name')

    file_path = sys.argv[1]
    csv_name = sys.argv[2]

    xml_file = pathlib.Path(file_path)
    if xml_file.is_file():
        xml_to_csv(file_path, csv_name)
    else:
        sys.exit(f'Did not find {file_path}')