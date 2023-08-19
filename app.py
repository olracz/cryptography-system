from flask_cors import CORS
from flask import Flask, request, jsonify
from MainController import CMainController

import logging
from logging.handlers import RotatingFileHandler
import sys

app = Flask(__name__)
CORS(app)

# Define a function to configure logging
def configure_logging():
    # (Your logging configuration code here, as before...)

# Rest of your Flask code...

    logger = logging.getLogger('flask_app')
    logger.setLevel(logging.DEBUG)

    # Define separate formats for console and log file
    console_format = '%(levelname)s: %(message)s'
    log_file_format = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'

    # Create a console handler with the console format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(console_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Create a file handler with the log file format
    log_filename = 'project_logs.log'
    file_handler = RotatingFileHandler(log_filename, maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(log_file_format)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    return logger

# Configure logging
logger = configure_logging()

main_controller = CMainController()

@app.route('/encrypt', methods=['GET'])
def encrypt_message():
    try:
        message = request.args.get('message')

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

@app.route('/decrypt', methods=['GET'])
def decrypt_message():
    try:
        encrypted_text = request.args.get('encrypted_text')

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
    app.run(debug=True)
