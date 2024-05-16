# badc_csv.py
import csv
import sys

from midas import extract_midas_metadata, UnknownMetadataLabelError

def parse_badc_csv(file_path):
    data_rows = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        in_data_section = False
        
        for row in reader:
            if not in_data_section:
                if row and row[0].strip().lower() == 'data':
                    in_data_section = True
                    # Read the column headers
                    column_headers = next(reader)
                continue
            
            if row and row[0].strip().lower() == 'end data':
                break
            
            data_row = dict(zip(column_headers, row))
            data_rows.append(data_row)
    
    return data_rows

def parse_badc_csv_metadata(file_path):
    metadata = {}
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row and row[0].strip().lower() == 'data':
                break

            if len(row) >= 3:
                label = row[0].strip()
                reference = row[1].strip()
                values = [val.strip() for val in row[2:]]
                metadata.setdefault(label, []).append((reference, values))

    return metadata
