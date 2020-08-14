from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port = '6379', db=0)


### If static string ####
redis.set('kochava', 'Star'.encode('utf-8'))

@app.route('/')
def hello():
    return 'The meaning of "Kochava" is %s.' % (redis.get('kochava').decode('utf-8'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
