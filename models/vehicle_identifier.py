from dataclasses import dataclass, asdict

from dataclasses_avroschema import AvroModel


@dataclass
class Vehicle(AvroModel):
    # Assuming your key has some unique identifier, e.g., car_id
    car_id: int

    def to_dict(self):
        return asdict(self)

    class Meta:
        namespace = "VehicleTelemetryKey.v1"
