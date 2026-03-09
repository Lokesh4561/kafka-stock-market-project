# Kafka Stock Market Data Pipeline

This project demonstrates a **real-time data engineering pipeline** using Apache Kafka and Python running on AWS EC2.

## Architecture

Python Producer
      ↓
Apache Kafka Topic
      ↓
Kafka Consumer
      ↓
AWS S3 Data Lake
      ↓
Amazon Athena Query

## Technologies Used

- Python
- Apache Kafka
- AWS EC2
- AWS S3
- Amazon Athena
- Kafka-Python
- Pandas

## Project Workflow

1. A Python **producer** sends stock market data.
2. Data is streamed into an **Apache Kafka topic**.
3. A **Kafka consumer** reads the streaming data.
4. The consumer can process and store data in **AWS S3**.
5. Data can then be queried using **Amazon Athena**.

## Project Structure

kafka-stock-market-project
│
├── producer.py       # Sends stock market data to Kafka
├── consumer.py       # Reads streaming data from Kafka
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation

## Example Streaming Data
AAPL,189
TSLA,245
GOOGLE,138
AMZN,175
MSFT,420
## Example Output

### Producer Streaming Data

![Producer Output](screenshots/producer_output.png)

### Consumer Receiving Data

![Consumer Output](screenshots/consumer_output.png)

## Author
Lokesh Reddy  
Master’s in Information Technology Management  
Aspiring Data Engineer  
United States

