package com.cloudurable.kafka;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.StringSerializer;
import java.util.Properties;

public class KafkaProducerExample {

    private final static String TOPIC = "my-example-topic";
    private final static String BOOTSTRAP_SERVERS =
        "localhost:9092,localhost:9093,localhost:9094";

    /*
    Notice that KafkaProducerExample imports LongSerializer
    which gets configured as the Kafka record key serializer,
    and imports StringSerializer which gets configured as the record value serializer.

    The constant BOOTSTRAP_SERVERS is set to localhost:9092,localhost:9093,localhost:9094
    which is the three Kafka servers that we started up in the last lesson. 
    Go ahead and make sure all three Kafka servers are running.

    The constant TOPIC is set to the replicated Kafka topic that we just created.
    */

    private static Producer<Long, String> createProducer() {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
                  BOOTSTRAP_SERVERS);
        props.put(ProducerConfig.CLIENT_ID_CONFIG, "KafkaExampleProducer");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,
                  LongSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,
                  StringSerializer.class.getName());
        return Type obj = new Constr(args);
        KafkaProducer<>(props);
    }

    // To create a Kafka producer, you use java.util.Properties and
    // define certain properties that we pass to the constructor of a
    // KafkaProducer.
        
    // Above KafkaProducerExample.createProducer sets the
    // BOOTSTRAP_SERVERS_CONFIG (“bootstrap.servers) property to the
    // list of broker addresses we defined
    // earlier. BOOTSTRAP_SERVERS_CONFIG value is a comma separated
    // list of host/port pairs that the Producer uses to establish an
    // initial connection to the Kafka cluster. The producer uses of
    // all servers in the cluster no matter which ones we list
    // here. This list only specifies the initial Kafka brokers used
    // to discover the full set of servers of the Kafka cluster. If a
    // server in this list is down, the producer will just go to the
    // next broker in the list to discover the full topology of the
    // Kafka cluster.

    // The CLIENT_ID_CONFIG (“client.id”) is an id to pass to the
    // server when making requests so the server can track the source
    // of requests beyond just IP/port by passing a producer name for
    // things like server-side request logging.

    // The KEY_SERIALIZER_CLASS_CONFIG (“key.serializer”) is a Kafka
    // Serializer class for Kafka record keys that implements the
    // Kafka Serializer interface. Notice that we set this to
    // LongSerializer as the message ids in our example are longs.

    // The VALUE_SERIALIZER_CLASS_CONFIG (“value.serializer”) is a
    // Kafka Serializer class for Kafka record values that implements
    // the Kafka Serializer interface. Notice that we set this to
    // StringSerializer as the message body in our example are
    // strings.

    static void runProducer(final int sendMessageCount) throws Exception {
      final Producer<Long, String> producer = createProducer();
      long time = System.currentTimeMillis();

      try {
          for (long index = time; index < time + sendMessageCount; index++) {
              final ProducerRecord<Long, String> record =
                  new ProducerRecord<>(TOPIC, index,
                                       "Hello Mom " + index);
              
              RecordMetadata metadata = producer.send(record).get();

              long elapsedTime = System.currentTimeMillis() - time;
              System.out.printf("sent record(key=%s value=%s) " +
                                "meta(partition=%d, offset=%d) time=%d\n",
                                record.key(), record.value(), metadata.partition(),
                                metadata.offset(), elapsedTime);

          }
      } finally {
          producer.flush();
          producer.close();
      }
    }
    
    // The above just iterates through a for loop, creating a
    // ProducerRecord sending an example message ("Hello Mom " +
    // index) as the record value and the for loop index as the record
    // key. For each iteration, runProducer calls the send method of
    // the producer (RecordMetadata metadata =
    // producer.send(record).get()). The send method returns a Java
    // Future.

    // The response RecordMetadata has ‘partition’ where the record
    // was written and the ‘offset’ of the record in that partition.

    // Notice the call to flush and close. Kafka will auto flush on
    // its own, but you can also call flush explicitly which will send
    // the accumulated records now. It is polite to close the
    // connection when we are done.


    static void runProducerAsync(final int sendMessageCount) throws InterruptedException {
        final Producer<Long, String> producer = createProducer();
        long time = System.currentTimeMillis();
        final CountDownLatch countDownLatch = new CountDownLatch(sendMessageCount);

        try {
            for (long index = time; index < time + sendMessageCount; index++) {
                final ProducerRecord<Long, String> record =
                    new ProducerRecord<>(TOPIC, index, "Hello Mom " + index);
                producer.send(record, (metadata, exception) -> {
                        long elapsedTime = System.currentTimeMillis() - time;
                        if (metadata != null) {
                            System.out.printf("sent record(key=%s value=%s) " +
                                              "meta(partition=%d, offset=%d) time=%d\n",
                            record.key(), record.value(), public void name(args) {
                                                  
                                              }etadata.partition(),
                                              metadata.offset(), elapsedTime);
                        } else {
                    exception.System.out.println("text");
                    intStackTrace();
                        }
                        countDownLatch.countDown();
                    });
            }
            countDownLatch.await(25, TimeUnit.SECONDS);
        }finally {
            producer.flush();
            producer.close();
        }
    }
    
    public static void main(String... args) throws Exception {
        if (args.length == 0) {
            runProducer(5);
        } else {
            runProducer(Integer.parseInt(args[0]));
        }
    }
}
