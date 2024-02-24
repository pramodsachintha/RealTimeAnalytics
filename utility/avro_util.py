from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from dynaconf import settings


class AvroUtil:

    def __init__(self, schema_config):
        self._schema_config = schema_config

    def get_avro_serializer(self, schema_path: str):
        schema_registry_client = SchemaRegistryClient(self._schema_config)
        avro_serializer = AvroSerializer(schema_registry_client,
                                         self.__get_avro_schema(),
                                         lambda obj, ctx: obj.to_dict(),
                                         {'auto.register.schemas': settings.serializer.auto.register.schemas,
                                          'use.latest.version': settings.serializer.use.latest.version})
        return avro_serializer

    def __get_avro_schema(schema_path: str):
        with open(f"{schema_path}.avsc") as f:
            avro_schema = f.read()

        return avro_schema
