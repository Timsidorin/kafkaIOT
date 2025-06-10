

import random
import time
import json
import threading
from abc import  ABC,abstractmethod
from dataclasses import dataclass
from typing import Dict, Any
from confluent_kafka import Producer




@dataclass
class SensorReading:
    sensor_id:str
    sensor_type:str
    timestamp: float
    data: Dict[str, Any]



class BaseSensor(ABC):
    """азовый класс для датчиков"""
    def __init__(self, sensor_id:str, update_interval: float = 5.0):
        self.sensor_id = sensor_id
        self.update_interval = update_interval
        self.is_running = False
        self.thread = None


    @abstractmethod
    def generate_data(self)-> Dict[str, Any]:
        """Генерация тестовых данных для датчика"""
        pass

    @abstractmethod
    def get_sensor_type(self) -> str:
        """Генерация тестовых данных для датчика"""
        pass


    def create_reading(self) -> SensorReading:
        """Обьект показания датчика"""
        return  SensorReading(
            sensor_id= self.sensor_id,
            sensor_type= self.get_sensor_type(),
            timestamp= time.time(),
            data = self.generate_data()
        )


    def start(self, producer: Producer, topic: str):
        """Запуск датчика в потоке"""
        self.is_running = True
        self.thread = threading.Thread(
            target= self._run_sensor,
            args=(producer,topic)
        )
        self.thread.start()


    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()



    def _run_sensor(self, producer: Producer, topic:str):
        """Цикл работы датчика"""
        while self.is_running:
            try:
                reading = self.create_reading()
                message = {
                    'sensor_id':reading.sensor_id,
                    'sensor_type': reading.sensor_type,
                    'timestamp': reading.timestamp,
                    'data': reading.data
                }

                producer.produce(
                    topic,
                    key=reading.sensor_id,
                    value=json.dumps(message)

                )

                producer.flush()
                print(f"[{reading.sensor_id}] Отправил: {reading.data}")
                time.sleep(self.update_interval)

            except Exception as e:
                print(f"Ошибка в датчике {self.sensor_id}: {e}")
                time.sleep(1)



