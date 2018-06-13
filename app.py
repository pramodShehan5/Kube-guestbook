from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host=os.environ.get('GET_HOSTS_FROM', 'env'), port=6379)
redis1 = Redis(host=os.environ.get('REDIS_MASTER_SERVICE_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    redis1.incr('hits')
    return 'Hello Container World! I have been seen %s times.\n' % redis1.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
