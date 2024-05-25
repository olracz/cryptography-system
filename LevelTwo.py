import os
import logging
from dotenv import load_dotenv
from xor_cipher import XORCipher
load_dotenv()


logging.basicConfig(
    filename='project_logs.log',  # Specify the log file
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format='%(asctime)s  - %(levelname)s - %(message)s'  # Specify log message format
)


class CLevelTwoEncryption:

    def __init__(self, level=2):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}')

        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__XOR_Key = bytes.fromhex(xor_key_hex)

    def encrypt(self, encrypted_bytes):
        encrypted_text = XORCipher.encrypt(encrypted_bytes, self.__XOR_Key)
        print("E_text2: ", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = XORCipher.decrypt(encrypted_text, self.__XOR_Key)
        print("D_text2: ", decrypted_text)
        return decrypted_text
