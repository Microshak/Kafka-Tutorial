# CLI
To use this tutorial you will need to exec into the Kafka container.

## Create a topic
```sh
kafka-topics --topic demo --partitions 3 --replication-factor 1 --create --bootstrap-server localhost:9092

```

## List Topics
```sh
kafka-topics --list  --bootstrap-server localhost:9092

```

## List Topics
```sh
kafka-topics --topic demo --describe --bootstrap-server localhost:9092

```

## Increase the number of partitions
```sh
kafka-topics --topic demo --partitions 5 --replication-factor 1 --create --bootstrap-server localhost:9092

```

## Produce Message to a topic
```
kafka-console-producer --bootstrap-server localhost:9092 --topic demo

```

## Consumer a message from a topic
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic demo

```


## Consumer a message from a topic from the beginning 
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic demo --from-beginning

```
