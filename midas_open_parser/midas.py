"""
midas
=====

This module provides functionality for extracting MIDAS metadata from the parsed
BADC-CSV metadata.
"""
from collections import defaultdict

class UnknownMetadataLabelError(Exception):
    """An exception raised when an unknown metadata label is encountered during
    metadata extraction.
    """
    pass

class LabelHandler:
    """The base class for handling metadata labels."""

    def handle_global(self, values):
        """Handle global metadata labels.

        Args:
            values (list): The list of values associated with the global metadata label.

        Returns:
            list: The processed values for the global metadata label.
        """

        return values

    def handle_field(self, field_name, values, label):
        """Handle field-level metadata labels.

        Args:
            field_name (str): The name of the field associated with the metadata label.
            values (list): The list of values associated with the field-level metadata label.
            label (str): The metadata label being handled.

        Returns:
            dict: A dictionary containing the processed field-level metadata.
        """
        raise UnknownMetadataLabelError(f"Unknown field-level metadata label: {label}")


class ConventionsHandler(LabelHandler):
    def handle_global(self, values):
        return dict(zip(values[::2], values[1::2]))

class TitleHandler(LabelHandler):
    def handle_global(self, values):
        # Assuming the title is a single string value
        return values[0] if values else None

class SourceHandler(LabelHandler):
    pass  # No special handling needed, use base class

class CreatorHandler(LabelHandler):
    pass  # No special handling needed, use base class

class ActivityHandler(LabelHandler):
    pass  # No special handling needed, use base class

class FeatureTypeHandler(LabelHandler):
    pass  # No special handling needed, use base class

class ObservationStationHandler(LabelHandler):
    pass  # No special handling needed, use base class

class LocationHandler(LabelHandler):
    def handle_global(self, values):
        location_data = {}
        if len(values) == 1:
            location_data['name'] = value
        elif len(values) == 2:
            lat, lon = values
            location_data['latitude'] = float(lat)
            location_data['longitude'] = float(lon)
        else:
            n, w, s, e = values
            location_data['bounding_box'] = {
                'north': float(n),
                'west': float(w),
                'south': float(s),
                'east': float(e),
            }
        return location_data

class CollectionNameHandler(LabelHandler):
    pass  # No special handling needed, use base class

class CollectionVersionNumberHandler(LabelHandler):
    pass  # No special handling needed, use base class

class DateValidHandler(LabelHandler):
    pass  # No special handling needed, use base class

class HistoryHandler(LabelHandler):
    pass  # No special handling needed, use base class

class LastRevisedDateHandler(LabelHandler):
    pass  # No special handling needed, use base class

class LongNameHandler(LabelHandler):
    def handle_field(self, field_name, values, label):
        return {field_name: {'long_name': values}}

class TypeHandler(LabelHandler):
    def handle_field(self, field_name, values, label):
        return {field_name: {'type': values[0]}}

class CommentsHandler(LabelHandler):
    def handle_field(self, field_name, values, label):
        return {field_name: {'comments': values}}

class CoordinateVariableHandler(LabelHandler):
    def handle_field(self, field_name, values, label):
        return {field_name: {'coordinate_variable': values}}

class SrcIdHandler(LabelHandler):
    def handle_global(self, values):
        return values[0]

class HistoricCountyNameHandler(LabelHandler):
    def handle_global(self, values):
        return values[0]

class HeightHandler(LabelHandler):
    def handle_global(self, values):
        return { 'value': values[0], 'unit': values[1]}

class MidasQcVersionNumberHandler(LabelHandler):
    def handle_global(self, values):
        return values[0]

class MidasStationIdHandler(LabelHandler):
    def handle_global(self, values):
        return values[0]

class MissingValueHandler(LabelHandler):
    def handle_global(self, values):
        return values[0]


# Create label handlers
default_label_handlers = {
    'Conventions': ConventionsHandler(),
    'title': TitleHandler(),
    'source': SourceHandler(),
    'creator': CreatorHandler(),
    'activity': ActivityHandler(),
    'feature_type': FeatureTypeHandler(),
    'observation_station': ObservationStationHandler(),
    'location': LocationHandler(),
    'collection_name': CollectionNameHandler(),
    'collection_version_number': CollectionVersionNumberHandler(),
    'date_valid': DateValidHandler(),
    'history': HistoryHandler(),
    'last_revised_date': LastRevisedDateHandler(),
    'comments': CommentsHandler(),
    'coordinate_variable': CoordinateVariableHandler(),
    'long_name': LongNameHandler(),
    'type': TypeHandler(),
    'src_id': SrcIdHandler(),
    'historic_county_name': HistoricCountyNameHandler(),
    'height': HeightHandler(),
    'midas_qc_version_number': MidasQcVersionNumberHandler(),
    'midas_station_id': MidasStationIdHandler(),
    'missing_value': MissingValueHandler(),
}

def extract_midas_metadata(metadata, label_handlers=default_label_handlers):
    """Extract MIDAS metadata from the parsed BADC-CSV metadata.

    Args:
        metadata (dict): The parsed BADC-CSV metadata dictionary.
        label_handlers (dict, optional): A dictionary containing instances of
        `LabelHandler` subclasses for handling specific metadata labels.

    Returns:
        dict: A dictionary containing the extracted MIDAS metadata, organized
        into global metadata (`midas_metadata['global']`) and field-level
        metadata (`midas_metadata[field_name]`).

    Raises:
        UnknownMetadataLabelError: If an unknown metadata label is encountered
        and there is no corresponding handler in `label_handlers`.
    """
    midas_metadata = defaultdict(lambda: defaultdict(dict))
    known_labels = set(label_handlers.keys())
    labels = set(metadata.keys())
    unknown_labels = labels - known_labels
    if(unknown_labels):
        raise UnknownMetadataLabelError(f"Unknown metadata labels: {unknown_labels}")

    for label, entries in metadata.items():
        if label not in known_labels:
            raise UnknownMetadataLabelError(f"Unknown metadata label: {label}")

        for reference, values in entries:
            if reference == 'G':
                # Global metadata
                midas_metadata['global'][label] = label_handlers[label].handle_global(values)
            else:
                field_name = (reference)
                handler = label_handlers.get(label)
                if handler:
                    field_data = handler.handle_field(field_name, values, label)
                    midas_metadata[field_name].update(field_data[field_name])
                else:
                    raise UnknownMetadataLabelError(f"Unknown field-level metadata label: {label}")

    return midas_metadata

