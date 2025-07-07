from feast import FeatureStore
from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource
)
from feast.types import Float32, Float64, Int64, String


RAW_DATA_FILEPATH = "./data/hotel_bookings.parquet"


# Entidad
booking = Entity(name="booking", join_keys=["booking_id"])


# File Source
booking_raw_source = FileSource(
    name="booking_raw_source",
    path=RAW_DATA_FILEPATH,
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)

booking_stats_fv = FeatureView(
    # The unique name of this feature view. Two feature views in a single
    # project cannot have the same name
    name="booking_monthly_stats",
    entities=[booking],
    # The list of features defined below act as a schema to both define features
    # for both materialization of features into a store, and are used as references
    # during retrieval for building a training dataset or serving features
    schema=[
        Field(name="avg_time", dtype=Float32),
    ],
    source=booking_raw_source,
    # Tags are user defined key/value pairs that are attached to each
    # feature view
    tags={"team": "booking_monthly"},
)