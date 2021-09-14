# Getting started

```sh
mkdir Producer
cd Producer
dotnet new console
dotnet add package Confluent.Kafka --version 1.7.0

```
## Create a producer
Open the project and put int the following code 

```dotnet
  using System;
using Confluent.Kafka;
using System.Net;
using System.Threading.Tasks;

namespace CCDAK
{
    class Program
    {
        static void  Main(string[] args) 
        {
            var pConfig = new ProducerConfig
            {
                BootstrapServers = "localhost",
                ClientId = Dns.GetHostName(),
            };

            ProduceAsync(pConfig).GetAwaiter().GetResult();
        }


         static async Task ProduceAsync(ProducerConfig pConfig)
         {
            using (var producer = new ProducerBuilder<string, string>(pConfig).Build())
            {
                var dr = await producer.ProduceAsync("myTopic", new Message<string, string> { Key = "1", Value = "Some Data" } )  ;
                Console.WriteLine($"Delivered '{dr.Value}' to '{dr.TopicPartitionOffset}'");
                
            }
         }
      }
}
```

## Create a consumer
cd into your Consumer directory


```sh
mkdir Consumer
cd Consumer
dotnet new console
dotnet add package Confluent.Kafka --version 1.7.0

```

Then in your program.cs file enter in: 

```dotnet

using Confluent.Kafka;
using System;
using System.Threading;


namespace KafakConsumer
{
    class Program
    {
        static void Main(string[] args)
        {
            var cConfig = new ConsumerConfig
            {
                BootstrapServers = "localhost",
                GroupId = "amikesGroupz",
            };

            using (var consumer = new ConsumerBuilder<string, string>(cConfig).Build())
               {
                consumer.Subscribe("myTopic");
                var consumeResult = consumer.Consume();
                Console.WriteLine($"consumed: {consumeResult.Message.Value}   partition: {consumeResult.Partition}");
            }
            
        }
    }
}

```

## Back Off Retry
Backoff allows you to resend a message if there is a failure.

> If you are trying to send messages in order and using async this can cause racetrack errors. You may want to ensure that your message is sent before the next one is sent.

```
   RetryBackoffMs = 1000,
```

## AKS
Acknowledgements now many servers need to respond to the producer before it responds.  These are:
* None
* 1
* All



```
Acks = Acks.All
```
