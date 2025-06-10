from random import choice, uniform
from typing import Dict, Any

from confluent_kafka import Producer

from Sensors import TemperatureSensor, HumiditySensor, PressureSensor


class SensorManager:
    def __init__(self, kafka_config: Dict[str,str]):
        self.producer    = Producer(kafka_config)
        self.sensors = []
        self.topic = 'IOT Датчики'


    def create_sensors(self, count:int = 1000):
        """Создание 1000 датчиков"""

        sensor_types = [TemperatureSensor, HumiditySensor, PressureSensor]

        for i in range(count):
            sensor_type = choice(sensor_types)
            sensor_id = f"{sensor_type.__name__.lower()}_{i:04d}"

            if sensor_type == TemperatureSensor:
                base_temp = uniform(18,30)
                sensor = sensor_type(sensor_id, base_temp = base_temp)

            else:
                sensor = sensor_type(sensor_id)

            self.sensors.append(sensor)


    def start_all_sensors(self):
        for sensor in self.sensors:
            sensor.start(self.producer, self.topic)


    def stop_all_sensors(self):
        for sensor in self.sensors:
            sensor.stop()




