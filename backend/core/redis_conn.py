from redis import Redis
from rq import Queue

redis = Redis(host="localhost", port=6379)
queue = Queue("inference", connection=redis)
