import os
from dotenv import load_dotenv

load_dotenv()

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

class CLevelThreeEncryption:

    def __init__(self, level=3):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}')

        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__XOR_Key = bytes.fromhex(xor_key_hex)

    def encrypt(self, encrypted_bytes):
        return XORCipher.encrypt(encrypted_bytes, self.__XOR_Key)

    def decrypt(self, input_text):
        return XORCipher.decrypt(input_text, self.__XOR_Key)
