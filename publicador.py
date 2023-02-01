import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.exchange_declare('exchange.eb77652a-f6fb-49be-8ec4-76cd50f5b1ed')  # declare exchange
channel.queue_declare(queue='exam', durable=True) # declare queue  
channel.queue_bind('exam', 'exchange.eb77652a-f6fb-49be-8ec4-76cd50f5b1ed', 'eb77652a-f6fb-49be-8ec4-76cd50f5b1ed') # create binding between queue and exchange

# publish message
channel.basic_publish(
  body='Hi CloudAMQP, this was fun!',
  exchange='exchange.eb77652a-f6fb-49be-8ec4-76cd50f5b1ed',
  routing_key='eb77652a-f6fb-49be-8ec4-76cd50f5b1ed',
   properties=pika.BasicProperties(delivery_mode=2,)
  )
print(' Message sent.')
channel.close()
connection.close()