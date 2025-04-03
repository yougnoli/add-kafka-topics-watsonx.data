# Kafka Streaming to Watsonx.data

This repository provides a practical demonstration on how to integrate real-time Kafka streams into IBM Watsonx.data, using IBM Cloud Event Streams (Lite plan). It includes detailed instructions, a Python Kafka producer example, and configuration files necessary to set up and query real-time data streams.

## Overview

- **IBM Cloud Event Streams**: Set up using the free Lite plan.
- **Kafka Topic**: `iss-data`, used as an example to stream the ISS's real-time position.
- **Kafka Producer**: Python script fetching data from a public ISS API and streaming it to Kafka.
- **Watsonx.data Integration**: Steps and JSON configuration to register Kafka as a data source and query real-time data.

## Content

- `producer.py`: Python script for real-time data ingestion from ISS API into Kafka.
- `kafka-topic.json`: JSON configuration to register your Kafka topic in Watsonx.data.

## Quick Start

1. **Setup IBM Cloud Event Streams**
   - Choose the Lite (free) plan.
   - Create the `iss-data` topic.
   - Generate service credentials.

2. **Kafka Producer Setup**
   - Install dependencies:  
     ```bash
     pip install confluent-kafka requests
     ```
   - Configure `producer.py` with your Kafka credentials and run the script:
     ```bash
     python producer.py
     ```

3. **Connect to Watsonx.data**
   - Add a Kafka data source via Watsonx.data Infrastructure Manager.
   - Upload the provided `kafka-topic.json` using the \"Add Topic\" option.

4. **Query Data**
   - Use Watsonx.data SQL interface to query real-time data
