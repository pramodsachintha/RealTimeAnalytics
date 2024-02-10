import unittest

from models.vehicle_identifier import Vehicle
from models.vehicle_info import VehicleInfo
from models.vehicle_telemetry import VehicleTelemetry
from utility.data_generator import DataGenerator
from utility.data_mapper import DataMapper


class DataMapperTests(unittest.TestCase):
    def test_key_mapping(self):
        dto = DataGenerator.generate_random_list(VehicleInfo, 1)[0]
        data_mapper = DataMapper[VehicleInfo, Vehicle, VehicleTelemetry](dto, Vehicle, VehicleTelemetry)
        key = data_mapper.get_key()
        self.assertEqual(key.car_id, dto.car_id)  # add assertion here

    def test_value_mapping(self):
        dto = DataGenerator.generate_random_list(VehicleInfo, 1)[0]
        data_mapper = DataMapper[VehicleInfo, Vehicle, VehicleTelemetry](dto, Vehicle, VehicleTelemetry)
        value = data_mapper.get_value()
        self.assertEqual(value.lap_time, dto.lap_time)
        self.assertEqual(value.session_time, dto.session_time)
        self.assertEqual(value.lap_distance, dto.lap_distance)
        self.assertEqual(value.total_distance, dto.total_distance)
        self.assertEqual(value.x_position, dto.x_position)


if __name__ == '__main__':
    unittest.main()
