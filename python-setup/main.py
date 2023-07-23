from flask import Flask, request, jsonify

app = Flask(__name__)

# Custom middleware to add CORS headers


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         'http://127.0.0.1:5500')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/greet', methods=['POST'])
def greet():
    try:
        data = request.get_json()
        input_string = data.get('input_string', None)

        if input_string is None:
            return jsonify({'error': 'Input string not provided'}), 400

        response = f"Hello , hi man, {input_string}"
        return jsonify({'message': response}), 200

    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Oops! Something went wrong.'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
