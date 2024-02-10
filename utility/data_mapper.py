from typing import TypeVar, Type, Generic, Any

from icecream import ic

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


class DataMapper(Generic[T, K, V]):

    def __init__(self, data_transfer_obj: T, key: K, value: V):
        self._data_transfer_object = data_transfer_obj
        self._key = key
        self._value = value

    def get_key(self):
        properties = self._key.__annotations__
        values = self.get_obj_values(properties)

        # Create an instance of the target type dynamically
        target_type = Type[K]
        mapped_data = type(target_type.__name__, (object,), values)()
        return mapped_data

    def get_obj_values(self, properties: Any):
        return {
            prop: getattr(self._data_transfer_object, prop) for prop in properties
        }

    def get_value(self):
        properties = self._value.__annotations__
        values = self.get_obj_values(properties)

        # Create an instance of the target type dynamically
        target_type = Type[V]
        mapped_data = type(target_type.__name__, (object,), values)()
        return mapped_data
