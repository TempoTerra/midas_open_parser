# Usage

## Parsing BADC-CSV Files

The `midas_open_parser` library provides functions to parse BADC-CSV files and extract data records and metadata.

```python
from midas_open_parser import parse_badc_csv, parse_badc_csv_metadata

# Parse the BADC-CSV file
metadata = parse_badc_csv_metadata('path/to/file.csv')
data_rows = parse_badc_csv('path/to/file.csv')
```

## Extracting Metadata

Once you have parsed the BADC-CSV file and obtained the metadata,
you can extract the MIDAS metadata using the `extract_midas_metadata` function.

```python
from midas_open_parser import extract_midas_metadata

# Extract MIDAS metadata
midas_metadata = extract_midas_metadata(metadata)
```

The `midas_metadata` dictionary contains the extracted metadata,
organized into global metadata (`midas_metadata['global']`) and field-level
metadata (`midas_metadata[field_name]`).

## Handling Metadata Labels

The `midas_open_parser` library provides a flexible and extensible architecture
for handling various metadata labels. Each label is associated with a handler
class that defines how the metadata should be processed.

The library includes default handlers for commonly used metadata labels,
such as 'Conventions', 'title', 'source', 'creator', 'activity',
'feature_type', 'observation_station', 'location', 'collection_name',
'collection_version_number', 'date_valid', 'history', 'last_revised_date',
'comments', 'coordinate_variable', 'long_name', 'type', 'src_id',
'historic_county_name', 'height', 'midas_qc_version_number',
'midas_station_id', and 'missing_value'.


## Handling Unknown Metadata Labels

If the library encounters an unknown metadata label,
it will raise an `UnknownMetadataLabelError`. You can handle this error
by catching the exception and taking appropriate action.

```
from midas_open_parser import extract_midas_metadata, UnknownMetadataLabelError

try:
    midas_metadata = extract_midas_metadata(metadata)
except UnknownMetadataLabelError as e:
    print(f"Error: {e}")
```

## Extending the Library

You can extend the `midas_open_parser` library by creating new handler classes
for additional metadata labels. To create a new handler class, you need
to inherit from the LabelHandler base class and implement the `handle_global`
or `handle_field` methods, depending on whether the label is a global
or field-level metadata label.


```
from midas_open_parser.midas import LabelHandler

class NewLabelHandler(LabelHandler):
    def handle_global(self, values):
        # Implement logic for handling global metadata
        return processed_values

    def handle_field(self, field_name, values, label):
        # Implement logic for handling field-level metadata
        return {field_name: processed_values}
```
