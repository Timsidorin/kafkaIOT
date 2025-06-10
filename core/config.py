from betterconf import Config, field

class KafkaConfig(Config):
    PRODUCER_SERVER = field("KAFKA_SERVER_PRODUCER", default="localhost:9092")

cfg = KafkaConfig()
