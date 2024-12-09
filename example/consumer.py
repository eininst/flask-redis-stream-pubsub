import logging

from flask import Flask, current_app
from flask_redis_stream_pubsub.pubsub import Consumer, Msg

app = Flask(__name__)
app.config.from_object("example.config")
app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
    consumer = Consumer(__name__)

    @consumer.subscribe("hello_word")
    def hello_word(msg: Msg):
        current_app.logger.info(msg)


    @consumer.subscribe("hello_word_cron", cron="*/5 * * * * *")
    def hello_word_cron(msg: Msg):
        """ 每5秒执行一次 """
        current_app.logger.info(msg)


    consumer.init_app(app)
    consumer.run("consumer:app")
