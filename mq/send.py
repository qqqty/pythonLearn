import pika

con = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = con.channel()


for i in range(100):
    i += 1
    mess = 'hello ' + str(i)
    if i % 3 == 1:
        channel.basic_publish(exchange='log', routing_key='to_my_log', body=mess)
    else:
        channel.basic_publish(exchange='log', routing_key='to_o_log', body=mess)

con.close()


