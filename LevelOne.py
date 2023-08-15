import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
class EncryptionUtils:
    def __init__(self, xor_key, caesar_shift, prefix, suffix):
        self.__xor_key = xor_key
        self.__caesar_shift = caesar_shift
        self.__prefix = prefix
        self.__suffix = suffix

    @staticmethod
    def _apply_caesar_shift(text, shift):
        caesar_text = "".join(chr((ord(char) - 32 + shift) % 96 + 32) for char in text)
        return caesar_text

    @staticmethod
    def _apply_xor(text, xor_key):
        text_bytes = text.encode('utf-8')
        encrypted_bytes = [text_bytes[i] ^ xor_key[i % len(xor_key)] for i in range(len(text_bytes))]
        return bytearray(encrypted_bytes)

    def encrypt(self, input_text):
        plain_text = self.__prefix + input_text + self.__suffix
        caesar_text = self._apply_caesar_shift(plain_text, self.__caesar_shift)
        encrypted_text = self._apply_xor(caesar_text, self.__xor_key)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_bytes = bytearray()
        for i, byte in enumerate(encrypted_text):
            decrypted_byte = byte ^ self.__xor_key[i % len(self.__xor_key)]
            decrypted_bytes.append(decrypted_byte)

        caesar_text = "".join(chr(byte) for byte in decrypted_bytes)
        original_text = self._apply_caesar_shift(caesar_text, -self.__caesar_shift)
        decrypted_text = original_text[len(self.__prefix):-len(self.__suffix)]
        return decrypted_text


class CLevelOneEncryption:
    def __init__(self, level=1):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}', '')
        xor_key_bytes = bytes.fromhex(xor_key_hex)
        caesar_shift = int(os.getenv('CAESAR_SHIFT', ''))
        prefix = os.getenv('PREFIX', '')
        suffix = os.getenv('SUFFIX', '')

        self.__encryption_utils = EncryptionUtils(xor_key_bytes, caesar_shift, prefix, suffix)

    def encrypt(self, input_text):
        return self.__encryption_utils.encrypt(input_text)

    def decrypt(self, encrypted_text):
        return self.__encryption_utils.decrypt(encrypted_text)
