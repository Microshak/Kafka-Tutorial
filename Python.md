# Running multiple brokers
```
docker-compose  -f docker-compose-multiple.yaml up --build -d

```

# Create a topic with a replication factor of 3
```
kafka-topics --topic demo --partitions 3 --replication-factor 3 --create --bootstrap-server localhost:19092
```


# Install Dependencies
```
pip install kafka-python
```


# Create a python file

Create the following Producer.py file
```py
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=['localhost:19092'], 
    acks = 'all',
)

for somenumber in range(10000):
    future = producer.send("demo",somenumber.to_bytes(4,byteorder='big'), b'msg')
    
    
    # Block for 'synchronous' sends
    record_metadata = future.get(timeout=10)
   
    if somenumber % 100 == 0:
        print(somenumber)
    

```

## Change the acks

The acks affect speed and guaranteed delivery

In your python code change and run:

* acks = 0,
* acks = 1,
* acks = 'all',