PUBSUB_REDIS_URL = 'redis://:7c3cD505@r-2vc5fd2ly3uxdrlwh0pd.redis.cn-chengdu.rds.aliyuncs.com:6379/0'
PUBSUB_REDIS_OPTION = {
    'group':'pubsub_g1', #消息分组 -> redis XGROUP groupname
    'workers':10, #消费进程数
    'retry_count':32, #默认重试次数
    'timeout_second':300, #默认超时时间，未来超时时间消费成功，将进行重试
    'block_second': 6, #读取消息的阻塞时间 -> xreadgroup block=6
    'read_count': 16, #一次最多读取的消息数量 -> xreadgroup read_count=16
}