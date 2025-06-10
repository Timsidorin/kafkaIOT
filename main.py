import time

from SensorManager import SensorManager
from core.config import cfg

def main():
    kafka_config = {
        'bootstrap.servers': cfg.PRODUCER_SERVER ,
        'client.id': 'IOT Симулятор'
    }

    manager = SensorManager(kafka_config)

    manager.create_sensors(1000)

    try:
        manager.start_all_sensors()
        print("Датчики запущены")
        time.sleep(300)

    finally:
        manager.stop_all_sensors()
        print("Датчики остановлены")

if __name__ == "__main__":
    main()