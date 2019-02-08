import pika

class MQSender:
    def __init__(self,queue):
        self.queue = queue

    def send_message(self, items_scraped, total ):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        self.channel.basic_publish(exchange='', routing_key =self.queue, body = 'Scraped {0} items out of {1}'.format(items_scraped,total))
        self.connection.close()
