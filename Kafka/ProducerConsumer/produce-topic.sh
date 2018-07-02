$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic --property "parse.key=true" --property "key.separator=:"

