from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify(
        {
        'message': 'Hello World',
        'time': datetime.datetime.now().strftime("%I:%M%p %S on %B %d, %Y"),
        'Hostname': socket.gethostname(),
        'Message': 'You are doing well.'
        'env': '${{values.app-env}}',
        'app_name': '${{values.app-name}}',
        }
    )

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': "UP"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# '/api/v1/details'
# '/api/v1/healthz'