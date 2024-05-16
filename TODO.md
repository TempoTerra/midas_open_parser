# TODO

This file contains a list of tasks and improvements planned for the `midas_open_parser` project.

## Features Roadmap

- [ ] Implement output formats suitable for code generation, schema generation, validation
- [ ] Implement mechanisms for ingestion into databases (e.g. singer tap)
- [ ] Implement data validation and cleaning functionality
- [ ] Add support for handling additional metadata labels specific to MIDAS Open
- [ ] Improve field handling in the MIDAS Open dataset (e.g. parse timestamps)

## Outside of scope

- [ ] Extend the library to support other atmospheric data formats (e.g., NetCDF, GRIB)
- [ ] Integrate with popular data analysis libraries (e.g., pandas, xarray)
- [ ] Develop a graphical user interface (GUI) for easy file selection and parsing

## Performance

- [ ] Explore performance optimizations for parsing large BADC-CSV files
- [ ] Investigate the possibility of parallel processing for metadata extraction
- [ ] Implement a caching mechanism for parsed metadata to improve performance

## Chores

- [ ] Add error handling for file I/O operations (e.g., `FileNotFoundError`)
- [ ] Add unit tests for the `badc_csv` module
- [ ] Implement a logging mechanism for better debugging and monitoring

## Documentation

- [ ] Add docstrings and comments to improve code readability and maintainability
- [ ] Create a comprehensive user guide and API documentation
- [ ] Provide usage examples and sample code snippets

