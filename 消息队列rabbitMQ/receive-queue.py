import pika

# 建立连接
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.77', credentials=credentials))

# 建立通道
channel = connection.channel()

# 声明队列
channel.queue_declare(queue='hello')


# 回调函数
def callback(ch, method, properties, body):
    print("从hello队列收到消息：%s"%body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 创建消费者
channel.basic_consume(callback,
                      queue='hello'
                      )  # 此消费者在hello队列上


channel.start_consuming()  # 开始轮询
