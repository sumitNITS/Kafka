## Setup and Test Kafka in Local Environment

## Requirements: 

VS Code (because it's cool), Docker Desktop

## Basic Understanding
Kafka — It is an event streaming platform which enables users to collect, store, and process data to build real-time event-driven applications which is written in Java and Scala.
</br></br>
Kafka broker — It is a single Kafka Cluster which is made of Brokers, They handle producers and consumers and keeps data replicated in the cluster.
</br></br>
Kafka topic — It is a category in which records are published. For example someone has a large blog site — here each blog category could be a single Kafka topic.
</br></br>
Kafka producer — It is an application (a piece of code) where we write to get data to Kafka.
</br></br>
Kafka consumer — It is a program where we write to get data out of Kafka. Sometimes a consumer is also a producer, as it puts data elsewhere in Kafka.
</br></br>
Zookeeper — It is Used to manage a Kafka cluster, track node status, and maintain a list of topics and messages.
</br></br>
Docker — It is an open-source platform for building, deploying, and managing containers. It allows us to package our applications into containers, which simplifies application distribution. That way, we know if the application works on our machine or not, it will work on any machine we deploy it to.
</br>
## Steps to Follow:
Step1:
In order to run kafka we will need two docker images below:</br></br>
Image 1: wurstmeister/zookeeper</br>
Image 2: wurstmeister/kafka</br>

But here we are doing it using docker compose. Check the kafka-docker-compose.yml file and save it.

step2:
Now use the command below to pull the two images and create containers for that:

#docker-compose -f kafka-docker-compose.yml up -d

step3:
Verify that both the containers are running fine using:

#docker ps

step4:
Now, start the kafka shell using the command below:

#docker exec -it kafka bash

step5:
In order to create the kafka topic move to:

#cd /opt/kafka_version-number>/bin

step6:
Use the command below to create the kafka topic:

#kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic topic_name

(Here topic_name will be the name of our topic. And since this is a test environment, we can keep replication-factor and partitions at 1, The replication-factor describes how many copies of data will be created and Partitions describes the number of brokers we want our data to be split between)

step7:
Use the below command to describe the kafka topic:

#kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic topic_name

step8:
Use the below command to delete the kafka topic:

#kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic topic_name

step9:
Use the below command to list the kafka topics:

#kafka-topics.sh --list --zookeeper zookeeper:2181

step10:
Use the below command to produce messages in a specified topic

#kafka-console-producer.sh --broker-list kafka:9092 --topic topic_name

step11:
Open a new terminal and goto:

#cd /opt/kafka_<version>/bin

step12:
Use the below command to consume any message for a specified topic

#kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic topic_name

step13:
In order to see all messages which is send to a specific topic, use the command:

#kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic topic_name --from-beginning

Cool, We are done here!
