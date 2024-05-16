"""
midas_open_parser
=================

A Python library for parsing BADC-CSV files from the MIDAS Open dataset.

This library provides a flexible and extensible framework for handling various
metadata labels and structures found in the MIDAS Open dataset.
"""

__version__ = "0.1.0"
__author__ = "Vanuan"
__email__ = "vanuan+midasparser@gmail.com"

from .badc_csv import parse_badc_csv, parse_badc_csv_metadata
from .midas import extract_midas_metadata, UnknownMetadataLabelError

__all__ = [
    "parse_badc_csv",
    "parse_badc_csv_metadata",
    "extract_midas_metadata",
    "UnknownMetadataLabelError",
]
