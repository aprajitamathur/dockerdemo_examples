import time
import redis
from flask import Flask,request,render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/<name>')
def hello_name(name):
    count = get_hit_count()
    return 'Hello {}! I have been seen {} times.\n'.format(name, count)


@app.route('/', methods=["POST"])
def some_function():
    text = request.form.get('name')
    count = get_hit_count()
    return 'Hello {}! I have been seen {} times.\n'.format(text, count)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
