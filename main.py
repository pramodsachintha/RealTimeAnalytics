# This is a sample Python script.
from dataclasses import fields

from icecream import ic

from models.vehicle_identifier import Vehicle
from models.vehicle_telemetry import VehicleTelemetry
from utility.data_generator import DataGenerator


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(Vehicle.avro_schema())
    print(VehicleTelemetry.avro_schema())
    sample_data = DataGenerator.generate_random_list(VehicleTelemetry, 50)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
