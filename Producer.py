from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=['localhost:19092'], 
  
)

for somenumber in range(100000000000):
    future = producer.send("demo",somenumber.to_bytes(4,byteorder='big'), b'msg')
    
    
    # Block for 'synchronous' sends
    record_metadata = future.get(timeout=10)
   
    if somenumber % 100 == 0:
        print(somenumber)
    