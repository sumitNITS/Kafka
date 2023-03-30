### Requirements: 

- VS Code or any other!
- Docker

### Basic Understanding

- Kafka: It is an event streaming platform which enables users to collect, store, and process data to build real-time event-driven applications which is written in Java and Scala.

- Kafka broker: It is a single Kafka Cluster which is made of Brokers, They handle producers and consumers and keeps data replicated in the cluster.

- Kafka topic: It is a category in which records are published. For example someone has a large blog site — here each blog category could be a single Kafka topic.

- Kafka producer: It is an application (a piece of code) where we write to get data to Kafka.

- Kafka consumer: It is a program where we write to get data out of Kafka. Sometimes a consumer is also a producer, as it puts data elsewhere in Kafka.

- Zookeeper: It is Used to manage a Kafka cluster, track node status, and maintain a list of topics and messages.

- Docker: It is an open-source platform for building, deploying, and managing containers. It allows us to package our applications into containers, which simplifies application distribution. That way, we know if the application works on our machine or not, it will work on any machine we deploy it to.

### Steps to Follow:

Step1: In order to run kafka we will need two docker images below

- Image 1: wurstmeister/zookeeper
- Image 2: wurstmeister/kafka

But here we are doing it using docker compose. Check the docker-compose.yml file and save it.

Step2: Use the command below to pull the two images and create containers for that

```bash
docker-compose -f docker-compose.yml up -d
```

Step3: Verify that both the containers are running fine using the command below

```bash
docker ps
```

Step4: Start the kafka shell using the command below

```bash
docker exec -it kafka bash
```

Step5: In order to create the kafka topic you need to move to

```bash
cd /opt/kafka_version-number/bin
```

Step6: Use the command below to create the kafka topic

```bash
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic topic_name
```

(Here topic_name will be the name of our topic. And since this is a test environment, we can keep replication-factor and partitions at 1, The replication-factor describes how many copies of data will be created and Partitions describes the number of brokers we want our data to be split between)

Step7: Use the below command to describe the kafka topic

```bash
kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic topic_name
```

Step8: Use the below command to delete the kafka topic

```bash
kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic topic_name
```

Step9: Use the below command to list the kafka topics

```bash
kafka-topics.sh --list --zookeeper zookeeper:2181
```

Step10: Use the below command to produce messages in a specified topic

```bash
kafka-console-producer.sh --broker-list kafka:9092 --topic topic_name
```

Step11: Open a new terminal and goto

```bash
cd /opt/kafka_<version>/bin
```

Step12: Use the below command to consume any message for a specified topic

```bash
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic topic_name
```

Step13: In order to see all messages which is send to a specific topic, use the command

```bash
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic topic_name --from-beginning
```

Cool, We are done here!

### Kafka Message automation using python

### Steps to Follow:

- Step1: Save the generator.py, producer.py and consumer.py files

- Step2: Setup and activate the virtualenv using the below 

```bash
pip install virtualenv
```

```bash
python -m virtalenv name_of_environment 
```

```bash
.\name_of_environment\Scripts\activate
```

- Step3: Run the below commands

```bash
pip install kafka-python
```

```bash
python consumer.py
```

Open the below command in a new terminal and observer consumer.py which is running in different terminal

```bash
python producer.py 
```

Cool, that's it!

