from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
    # app.run(ssl_context='adhoc')
