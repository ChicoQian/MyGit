D:
CD D:\JAVAEE.DEV\kafka\kafka_2.9.2-0.8.2.1
.\bin\windows\kafka-server-start.bat .\config\server.properties
CD bin
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test