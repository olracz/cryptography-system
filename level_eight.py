import base64
import os
import logging
from dotenv import load_dotenv
from xor_cipher import XORCipher

load_dotenv()


# Configure logging to write errors to the project_logs file
logging.basicConfig(
    filename='project_logs.log',
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class CLevelEightEncryption:
    def __init__(self, level=8):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}')

        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__XOR_Key = bytes.fromhex(xor_key_hex)

    def encrypt(self, encrypted_bytes):
        encrypted_text = XORCipher.encrypt(encrypted_bytes, self.__XOR_Key)
        encoded_result = base64.urlsafe_b64encode(encrypted_text).decode()
        print("E_text8: ", encoded_result)
        return encoded_result

    def decrypt(self, encrypted_text):
        decoded_bytes = base64.urlsafe_b64decode(encrypted_text)
        decrypted_text = XORCipher.decrypt(decoded_bytes, self.__XOR_Key)
        print("D_text8: ", decrypted_text)
        return decrypted_text
