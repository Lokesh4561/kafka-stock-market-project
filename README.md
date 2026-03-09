# Kafka Stock Market Data Pipeline

This project demonstrates a **real-time data engineering pipeline** using Apache Kafka and Python running on AWS EC2.

## Architecture

Producer (Python Script)  
↓  
Apache Kafka Topic  
↓  
Kafka Consumer  
↓  
Data Processing / Storage (AWS S3)  
↓  
Query using Amazon Athena

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

## Example Streaming Data

