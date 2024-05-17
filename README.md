# MIDAS Open parser

`midas_open_parser` is a Python library specifically designed to parse BADC-CSV files from the MIDAS Open dataset.

It provides a tailored and extensible framework for handling the metadata labels and structures found in the MIDAS Open dataset.

The main goal of the `midas_open_parser` project is to provide tools to ingest the MIDAS Open dataset into various destinations.

## About MIDAS Open and BADC-CSV

### MIDAS Open Dataset

The Met Office Integrated Data Archive System (MIDAS) Open dataset is a collection of surface observations from the UK land surface observing network. It includes various meteorological parameters such as temperature, wind, precipitation, and cloud cover, among others. The dataset is maintained and distributed by the Met Office, the national meteorological service for the UK.

For more information about the MIDAS Open dataset, please refer to the following resources:

- [MIDAS Open User Guide](https://help.ceda.ac.uk/article/4982-midas-open-user-guide)

### BADC-CSV Format

The BADC-CSV (British Atmospheric Data Centre Comma-Separated Values) format is a text-based format used to store and distribute data from the MIDAS Open dataset. It is a structured CSV format that includes a metadata section describing the data, followed by the actual data records.

The metadata section follows various conventions, such as the Climate and Forecast (CF) conventions, to provide detailed information about the data variables, units, measurement methods, and other relevant metadata. This metadata is crucial for properly interpreting and understanding the data.

For more information about the BADC-CSV format, please refer to the following resources:

- [Short description](https://help.ceda.ac.uk/article/105-badc-csv)
- [BADC-CSV GitHub repository](https://github.com/cedadev/badc-csv/tree/main)
- [The BADC Text File - Guide for users, and producers](https://github.com/cedadev/badc-csv/blob/main/new_ASCII_file_format_guide.md)

## Features

- Parse BADC-CSV files and extract data records
- Extract and process metadata from BADC-CSV files
- Support for handling global and field-level metadata
- Extensible architecture for adding new metadata label handlers
- Error handling for unknown metadata labels
- Command-line interface for running the parser

## Installation

You can install badc-csv-parser using pip:

```bash
pip install badc-csv-parser
```

## Usage

Here's an example of how to use badc-csv-parser:

```python
from badc_csv_parser import parse_badc_csv, parse_badc_csv_metadata
from midas import extract_midas_metadata

# Parse the BADC-CSV file metadata
metadata = parse_badc_csv_metadata('path/to/file.csv')

# Extract MIDAS metadata
midas_metadata = extract_midas_metadata(metadata)

# Access global metadata
print("Global Metadata:")
for field, values in midas_metadata['global'].items():
    print(f"{field}: {values}")

# Access field metadata
print("\nField Metadata:")
for field_name, field_data in midas_metadata.items():
    if field_name != 'global':
        print(f"{field_name}: {field_data}")

# Parse the BADC-CSV data records
data_rows = parse_badc_csv('path/to/file.csv')
for row in data_rows:
    print(row)
```


You can also use the command-line interface:

```python
python -m badc_csv_parser.test path/to/file.csv
```

## License

This project is licensed under the MIT License.
