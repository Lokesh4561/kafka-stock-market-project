from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stocks = [
    {"symbol": "AAPL", "price": 189},
    {"symbol": "TSLA", "price": 245},
    {"symbol": "GOOGLE", "price": 138}
]

for stock in stocks:
    producer.send("stock_market", stock)
    print("Sent:", stock)
    time.sleep(2)
