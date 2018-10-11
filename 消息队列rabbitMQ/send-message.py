import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.1.77', credentials=credentials))
channel = connection.channel()

# 交换机声明
channel.exchange_declare(exchange='subscriber',
                         exchange_type='fanout')

# 声明queue
# channel.queue_declare(queue='hello')

# 绑定队列到交换机
# channel.queue_bind(exchange='logs', queue='hello')

# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='subscriber',
                      routing_key='',
                      body='test subscriber-publisher',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent#消息持久化
                      )
                      )
print(" 消息发送成功！")
connection.close()