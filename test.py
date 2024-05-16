# test.py
import csv
import sys

from midas import extract_midas_metadata, UnknownMetadataLabelError
from badc_csv import  parse_badc_csv, parse_badc_csv_metadata

if __name__ == '__main__':
    print('hello')

    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please provide a filepath as input")
        sys.exit(-1)

    try:
        metadata = parse_badc_csv_metadata(filename)
        midas_metadata = extract_midas_metadata(metadata)
    except UnknownMetadataLabelError as e:
        print(f"Error: {e}")
        sys.exit(-1)

    print("Global Metadata:")
    for field, values in midas_metadata['global'].items():
        print(f"  {field}: {values}")

    print("\nField Metadata:")
    for field_name, field_data in midas_metadata.items():
        if field_name == 'global':
            continue  # Skip the 'global' key
        print(f"{field_name}: {field_data}")

    data = parse_badc_csv(filename)
#    for row in data:
#        print(row)
