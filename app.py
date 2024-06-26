from flask import Flask, request, jsonify
from flask_cors import CORS
from MainController import CMainController
import logging
from logging.handlers import RotatingFileHandler
import sys

app = Flask(__name__)
CORS(app)


# Define a function to configure logging
def configure_logging():

    logger = logging.getLogger('flask_app')
    logger.setLevel(logging.DEBUG)

    # Define log format
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    log_formatter = logging.Formatter(log_format)

    # Create a file handler with the log file format
    log_filename = 'project_logs.log'
    file_handler = RotatingFileHandler(log_filename, maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    # Filter out Werkzeug server log messages
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.ERROR)  # Set level to ERROR to filter out INFO and WARNING messages

    return logger


# Configure logging
logger = configure_logging()

main_controller = CMainController()


@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    try:
        if request.content_type != "application/json":
            return jsonify({'error': 'Wrong content-type'}), 400
        data = request.get_json()
        message = data.get('message')

        logger.debug("Received request with message: %s", message)

        if not message:
            return jsonify({'error': 'Missing message parameter'}), 400

        encrypted_message = main_controller.encrypt(message)

        response = {
            'encrypted_message': encrypted_message
        }
        return jsonify(response), 200

    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    try:
        if request.content_type != "application/json":
            return jsonify({'error': 'Wrong content-type'}), 400
        data = request.get_json()
        encrypted_text = data.get('encrypted_text')

        logger.debug("Received request with encrypted text: %s", encrypted_text)

        if not encrypted_text:
            return jsonify({'error': 'Missing encrypted_text parameter'}), 400

        original_text = main_controller.decrypt(encrypted_text)

        response = {
            'original_text': original_text
        }
        return jsonify(response), 200

    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return jsonify({'error': 'An error occurred'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
