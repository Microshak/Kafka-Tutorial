

## Background

The Kafka broker is dependent on two things to start:

. A zookeeper node to connect to ([Pre-KIP-500](https://cwiki.apache.org/confluence/display/KAFKA/KIP-500%3A+Replace+ZooKeeper+with+a+Self-Managed+Metadata+Quorum))
. A properties file that provides it instruccions on what settings to enable/modify.

This repo is a testing environment to modify this properties file, which is commonly located under `/etc/kafka/server.properties`.

## Broker Settings

To modify the broker settings, one can do it in two ways:

. Through environment variables in the docker compose file attached.
. Through entering the container and modifying the underlying `server.properties`

We will be showing how to do number 2, but feel free to play around with it with modifications under number 1.

To start, we will be entering our container and modifying our properties file.

```sh
docker-compose exec broker /bin/bash
nano server.properties
```

It is important to note that the order in which you define the properties in the file does not matter expect for overriding (if two properties of the same name are defined, the one defined last takes precedence).

When you are done modifying the properties file, you can perform a `control + x` in order to save it.

### listeners

The listeners configuration maps a listener name to a network interface and port. If the listener name also happens to be a security protocol, it will default to that security protocol without needing to define `listener.security.protocol.map`.

`listeners=PLAINTEXT://:9092` <--- This listener defines a bind on the default interface, in port 9092, with the PLAINTEXT security protocol (No security)
`listeners=SASL_SSL://localhost:9093` <--- This listener defines a bind on the localhost interface, in port 9093, with the SASL_SSL security protocol (SASL auth, SSL encryption)
`listeners=EXTERNAL://0.0.0.0:9094` <--- This listener defines a bind on all interfaces, in port 9094, with no explicit security protocol, so it will have to be defined through `listener.security.protocol.map`

The listeners property can be comma separated to set-up multiple listeners.

### advertised.listeners

Unlike `listeners`, `advertised.listeners` defines where we tell Kafka clients how to connect to the broker itself (a.k.a. the "advertised adress" of the broker).
Advertised listeners are also tied to a listener name. For example, a proper set up for our previously set `listeners` example would be:

`advertised.listeners=PLAINTEXT://devel.broker.com:9092` <--- This listener should take the form of the hostname, we are assuming our hostname is `devel.broker.com`
`advertised.listeners=SASL_SSL://localhost:9093` <--- This listener defines a bind on the localhost interface, so it will only be accessible through the host itself.
`advertised.listeners=EXTERNAL://developer.confluent.io:9094` <--- This listener defines a bind on all interfaces, so it can be addressed however the operator chooses

The advertised.listeners property can also be comma separated to set-up multiple listeners.

### broker.id

UID for the broker, it must be unique within a cluster. The broker also has the capability to auto-generate this ID if unset.

`broker.id=1`

### log.dirs

A comma separated list of directories in the host where Kafka will store data sent by producers.

`log.dirs=/mnt/kafka/data`

### num.partitions

The default number of partitions a topic should be created with. This can be overriden by the user.

`num.partitions=3`

### auto.create.topics.enable

Whether the Kafka cluster should automatically create a topic if a client requests it and it does not exist.

`auto.create.topics.enable=false`

### unclean.leader.election.enable

Allows the election of replicas that are not caught up to the latest message to be selected leaders. Data loss is highly likely to occur, this is considered a last-resort setting for failure scenarios. False by default. This can be enabled on a per-topic basis as well.

`unclean.leader.election.enable=false`

## log.cleanup.policy

The policy Kafka will follow to delete old data in a topic. This can be enabled cluster-wide or per topic.

The `delete` policy is time-based or size-based retention, which means it will delete data after a configurable amount of time.
The `compact` policy is key-based, which means it will delete records that have the same key and only leave the latest one.

`log.cleanup.policy=delete`



