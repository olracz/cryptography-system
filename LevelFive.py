import base64
import os
from dotenv import load_dotenv

# Load the .env file from the root directory
load_dotenv()
class XORCipher:
    @staticmethod
    def encrypt(plaintext_bytes, xor_key):
        encrypted_bytes = bytearray()
        for i, byte in enumerate(plaintext_bytes):
            encrypted_byte = byte ^ xor_key[i % len(xor_key)]
            encrypted_bytes.append(encrypted_byte)

        encoded_result = base64.b64encode(encrypted_bytes).decode()
        print("Encoded result: ", encoded_result)
        return encoded_result

    @staticmethod
    def decrypt(input_text, xor_key):
        decoded_bytes = base64.b64decode(input_text)

        decrypted_bytes = bytearray()
        for i, byte in enumerate(decoded_bytes):
            decrypted_byte = byte ^ xor_key[i % len(xor_key)]
            decrypted_bytes.append(decrypted_byte)

        return decrypted_bytes

class CLevelFiveEncryption:
    def __init__(self, level=5):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}')

        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__XOR_Key = bytes.fromhex(xor_key_hex)

    def encrypt(self, encrypted_bytes):
        return XORCipher.encrypt(encrypted_bytes, self.__XOR_Key)

    def decrypt(self, input_text):
        return XORCipher.decrypt(input_text, self.__XOR_Key)
