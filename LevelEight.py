import base64
import os
import logging
from dotenv import load_dotenv


load_dotenv()


# Configure logging to write errors to the project_logs file
logging.basicConfig(
    filename='project_logs.log',
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class XORCipher:
    @staticmethod
    def encrypt(plaintext_bytes, xor_key):
        encrypted_bytes = bytearray()
        for i, byte in enumerate(plaintext_bytes):
            encrypted_byte = byte ^ xor_key[i % len(xor_key)]
            encrypted_bytes.append(encrypted_byte)

        encoded_result = base64.urlsafe_b64encode(encrypted_bytes).decode()
        return encoded_result

    @staticmethod
    def decrypt(input_text, xor_key):
        decoded_bytes = base64.urlsafe_b64decode(input_text)

        decrypted_bytes = bytearray()
        for i, byte in enumerate(decoded_bytes):
            decrypted_byte = byte ^ xor_key[i % len(xor_key)]
            decrypted_bytes.append(decrypted_byte)

        return decrypted_bytes


class CLevelEightEncryption:
    def __init__(self, level=8):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}')

        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__XOR_Key = bytes.fromhex(xor_key_hex)

    def encrypt(self, encrypted_bytes):
        encrypted_text = XORCipher.encrypt(encrypted_bytes, self.__XOR_Key)
        print("E_text8: ", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = XORCipher.decrypt(encrypted_text, self.__XOR_Key)
        print("D_text8: ", decrypted_text)
        return decrypted_text
