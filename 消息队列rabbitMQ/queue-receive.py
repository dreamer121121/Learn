#!/usr/bin/env python

# 发送消息
'''
import pika

credentials = pika.PlainCredentials('admin', 'admin')

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.1.77', 5672, '/', credentials))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')

# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
'''
# consumer
import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.1.77', credentials=credentials))
channel = connection.channel()

# 消费者里面要再一次声明交换机
channel.exchange_declare(exchange='subscriber',
                         exchange_type='fanout')

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.

# 声明队列

# 生成随机命名的队列结束后自动删除

# 产生随机的队列名
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 将队列绑定到交换机上
channel.queue_bind(exchange='subscriber', queue=queue_name)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 告诉发送端我已经处理完了消息队列就会删除该条信息

channel.basic_consume(callback,
                      queue=queue_name)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 启动消息轮询等待接收消息
