import math
import random
import time
from random import uniform as uni
from typing import Dict, Any

from BaseSensor import BaseSensor

class TemperatureSensor(BaseSensor):
    def _init__(self, sensor_id:str, base_temp:float = 22.0, variance:float = 5.0):
        super().__init__(sensor_id, update_interval=uni(3,7))

        self.base_temp = base_temp
        self.variance = variance

    def get_sensor_type(self) -> str:
        return "Температура"


    def generate_data(self) -> Dict[str, Any]:
        hour = time.localtime().tm_hour
        daily_variation = 3* math.sin(2 * math.pi * (hour-6) /24)
        temperature = self.base_temp + daily_variation + random.gauss(0,self.variance)

        return {
            "Температура": round(temperature,2),
            'Единица измерения': "Цельсия"

        }


class HumiditySensor(BaseSensor):
    def get_sensor_type(self) -> str:
        return "humidity"

    def generate_data(self) -> Dict[str, Any]:
        humidity = uni(30, 80)
        return {
            'Влажность': round(humidity, 1),
            'Единица измерения': '%'
        }


class PressureSensor(BaseSensor):
    def get_sensor_type(self) -> str:
        return "pressure"

    def generate_data(self) -> Dict[str, Any]:
        pressure = uni(990, 1030)
        return {
            'Давление': round(pressure, 2),
            'Единица измерения': 'Кпа'
        }