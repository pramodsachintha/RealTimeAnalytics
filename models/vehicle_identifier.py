from dataclasses import dataclass

from dataclasses_avroschema import AvroModel


@dataclass
class Vehicle(AvroModel):
    # Assuming your key has some unique identifier, e.g., car_id
    car_id: int

    class Meta:
        namespace = "VehicleTelemetryKey.v1"
