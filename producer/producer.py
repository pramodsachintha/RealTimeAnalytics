from abc import ABC
from typing import Generic, TypeVar, List

from confluent_kafka import SerializingProducer
from config import settings
from utility.data_mapper import DataMapper

T = TypeVar("T")


class Producer(Generic[T]):
    pass

    def __init__(self, produce_elements: List[T], topic: str) -> None:
        self._produce_items = produce_elements
        self._producer = SerializingProducer({
            'bootstrap.servers': settings.bootstrap.servers,
            'security.protocol': settings.security.protocol,
            'delivery.timeout.ms': 1000000
        })

    def produce_to_topic(self) -> None:
        """
        produces data to the topic
        :return:
        """
        for items in self._produce_items:
            key = DataMapper.get_key()
            value = DataMapper.get_value()
            
