import logging

from flask import Flask, current_app
from flask_redis_stream_pubsub.pubsub import Consumer, Msg, runs

app = Flask(__name__)
app.config.from_object("example.config")
app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
    cs = Consumer(__name__)


    @cs.subscribe("hello_word")
    def hello_word(msg: Msg):
        """ 业务代码没抛出异常, 就代表消费成功 """
        current_app.logger.info(msg)


    @cs.subscribe("hello_word_retry", retry_count=3, timeout=30)
    def hello_word_retry(msg: Msg):
        """ 重试3次, 每次间隔30秒 """
        current_app.logger.info(msg)
        raise RuntimeError("I will retry 3 times, with a 30 second interval between each attempt")


    @cs.subscribe("hello_word_cron", cron="*/5 * * * * *", retry_count=0)
    def hello_word_cron(msg: Msg):
        """ 每5秒执行一次, 不重试 """
        current_app.logger.info(msg)


    @cs.subscribe("hello_word_cron_15", cron="*/10 * * * * *", retry_count=0)
    def hello_word_cron_15(msg: Msg):
        """ 每15分钟执行一次, 不重试 """
        current_app.logger.info(msg)


    cs.init_app(app)
    cs.run("consumer:app")
