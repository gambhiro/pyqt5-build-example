import socket
import os
from flask import Flask, send_from_directory, abort
from flask_cors import CORS

from smallapp import PACKAGE_ASSETS_DIR
from smallapp import logger

app = Flask(__name__)
app.config['ENV'] = 'development'
cors = CORS(app)


@app.route('/assets/<path:path>', methods=['GET'])
def assets(path):
    if not os.path.isfile(os.path.join(PACKAGE_ASSETS_DIR, path)):
        abort(404)

    return send_from_directory(PACKAGE_ASSETS_DIR, path)

@app.errorhandler(400)
def resp_bad_request(e):
    msg = f"Bad Request: {e}"
    logger.error(msg)
    return msg, 400

@app.errorhandler(404)
def reps_not_found(e):
    msg = f"Not Found: {e}"
    logger.error(msg)
    return msg, 404

@app.errorhandler(403)
def resp_forbidden(e):
    msg = f"Forbidden: {e}"
    logger.error(msg)
    return msg, 403

def start_server(port=8000):
    logger.info(f'Starting server on port {port}')
    os.environ["FLASK_ENV"] = "development"
    app.run(host='127.0.0.1', port=port, debug=False, load_dotenv=False)

def find_available_port() -> int:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    _, port = sock.getsockname()
    return port
