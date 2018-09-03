from redis import Redis

_REDIS_SETTING = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 6
}

r = Redis(**_REDIS_SETTING)