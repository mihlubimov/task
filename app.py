from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

taskGet = [
    {
        "id": "10dcdccb-8876-4245-ac53-92900c6509bd",
        "title": "Первая заметка",
        "text": "Вторая заметка",
        "date_create": 1513759529,
        "date_update": 1517259529
    },
    {
        "id": "10dcdccb-8876-4245-ac53-92900c6509bd",
        "title": "Первая заметка",
        "text": "Вторая заметка",
        "date_create": 1513759529,
        "date_update": 1517259529
    }
]

taskT = [
    {
        'result': True
    }
]


@app.route('/', methods=['GET'])
def GET():
    if len(taskGet) == 0:
        abort(404)
    return jsonify(taskGet)


@app.route('/', methods=['POST'])
def POST():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = [
        {
            'title': request.json['title'],
            'text': request.json['text'],
            'result': True
        }
    ]
    return jsonify(task), 201


@app.route('/', methods=['PUT'])
def PUT():
    if not request.json or not 'id' in request.json:
        abort(400)
    return jsonify(taskT)


@app.route('/', methods=['DELETE'])
def DELETE():
    if not request.json or not 'id' in request.json:
        abort(400)
    return jsonify(taskT)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
