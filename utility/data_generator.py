from dataclasses import fields, is_dataclass, dataclass
from random import random, uniform, randint


@dataclass
class DataGenerator:
    @staticmethod
    def generate_random_object(data_class):
        field_values = {
            field.name: DataGenerator.generate_random_value(field.type)
            for field in fields(data_class)
        }
        return data_class(**field_values)

    @staticmethod
    def generate_random_value(data_type):
        if is_dataclass(data_type):
            return DataGenerator.generate_random_object(data_type)
        elif data_type == float:
            return uniform(0, 1000)
        elif data_type == int:
            return randint(0, 100)
        elif data_type == list:
            return [DataGenerator.generate_random_value(float) for _ in range(3)]  # Adjust for list types
        else:
            return None  # Handle other data types as needed

    @staticmethod
    def generate_random_list(data_class, size):
        return [DataGenerator.generate_random_object(data_class) for _ in range(size)]