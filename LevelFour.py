import os
import logging
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(
    filename='project_logs.log',  # Specify the log file
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Specify log message format
)


class XORCipher:

    @staticmethod
    def encrypt(plaintext_bytes, xor_key):

        encrypted_bytes = bytearray()
        for i, byte in enumerate(plaintext_bytes):
            encrypted_byte = byte ^ xor_key[i % len(xor_key)]
            encrypted_bytes.append(encrypted_byte)

        return encrypted_bytes

    @staticmethod
    def decrypt(encrypted_text, xor_key):

        decrypted_bytes = bytearray()
        for i, byte in enumerate(encrypted_text):
            decrypted_byte = byte ^ xor_key[i % len(xor_key)]
            decrypted_bytes.append(decrypted_byte)

        return decrypted_bytes

class CLevelFourEncryption:

    def __init__(self, level=4):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}')

        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__XOR_Key = bytes.fromhex(xor_key_hex)

    def encrypt(self, encrypted_bytes):
        encrypted_text = XORCipher.encrypt(encrypted_bytes, self.__XOR_Key)
        print("E_text4: ", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = XORCipher.decrypt(encrypted_text, self.__XOR_Key)
        print("D_text4: ", decrypted_text)
        return decrypted_text
