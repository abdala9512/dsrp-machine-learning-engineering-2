from feast import FeatureStore
from feast import (
    Entity,
    FeatureView,
    FileSource,
    Field,
    RequestSource,
    FeatureService,
)
from feast.types import Int64, Float64, String
from feast.on_demand_feature_view import on_demand_feature_view
import pandas as pd

booking = Entity(name="booking", join_keys=["booking_id"])


booking_source = FileSource(
    name="booking_source",
    path="./data/bookings_feature_table.parquet",
    timestamp_field="timestamp",
    created_timestamp_column="created",
)

booking_view = FeatureView(
    name="booking",
    entities=[booking],
    schema=[
        Field(name="booking_id", dtype=String),
        Field(name="great_feature1", dtype=Float64, description="This is a great feature"),
        Field(name="great_feature2", dtype=Float64, description="This is a great feature"),
    ],
    source=booking_source,
)

input_request = RequestSource(
    name="input_request",
    schema=[
        Field(name="booking_id", dtype=String),
    ],
)

@on_demand_feature_view(
    sources=[booking_view, input_request],
    schema=[
        Field(name="great_feature1", dtype=Float64),
        Field(name="great_feature2", dtype=Float64),
    ],
)
def great_feature_view(inputs: pd.DataFrame):
    return pd.DataFrame(
        {"great_feature1": [1.0, 2.0], "great_feature2": [3.0, 4.0]}
    )

dsrp_feature_service = FeatureService(
    name="dsrp_feature_service",
    features=[great_feature_view],
)