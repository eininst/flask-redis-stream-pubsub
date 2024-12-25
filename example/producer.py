from flask import Flask

from flask_redis_stream_pubsub.producer import Producer

app = Flask(__name__)
app.config.from_object("example.config")

if __name__ == '__main__':
    producer = Producer()

    producer.init_app(app)

    msgid = producer.publish("hello_word_retry", {'name': 'dog'})
    print(msgid)

    # 批量发送
    sess = producer.session
    sess.add("hello_word1", {'name': 'cat1'})
    sess.add("hello_word", {'name': 'cat2'})
    sess.add("hello_word", {'name': 'cat3'})
    sess.add("hello_word", {'name': 'cat4'})
    sess.add("hello_word", {'name': 'cat5'})

    msgids = sess.commit()
    print(msgids)
