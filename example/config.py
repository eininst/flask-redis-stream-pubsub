PUBSUB_REDIS_URL = 'redis://:password@r-host.redis.cn-chengdu.rds.aliyuncs.com:6379/0'
PUBSUB_REDIS_OPTION = {
    'group':'pubsub_g1',
    'workers':10,
    'retry_count':32,
    'timeout_second':300,
    'block_second': 5,
    'read_count': 16,
}