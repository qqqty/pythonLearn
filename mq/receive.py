import pika

con = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = con.channel()

channel.queue_bind(exchange='log', queue='my_log', routing_key='to_my_log')


def callback(ch, method, properties, body):
    print method.routing_key, body
    
    
channel.basic_consume(callback, queue='my_log', no_ack=True)

channel.start_consuming()
