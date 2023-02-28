from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/login", methods=['POST'])
def login():
    return {
        "user": 'xxx'
    }


@app.route("/blog/edit", methods=['POST'])
def edit():
    if not request.json:
        abort(400)
    if 'title' in request.json:
        pass
    else:
        abort(400)
    if 'content' in request.json:
        pass
    else:
        abort(400)
    blog = {
        'title': request.json['title'],
        'content': request.json['content']
    }
    return jsonify({'blog': blog}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
