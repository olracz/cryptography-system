import os
import logging
from dotenv import load_dotenv
from caesar_cipher import CaesarCipher
from xor_cipher import XORCipher

load_dotenv()


logging.basicConfig(
    filename='project_logs.log',  # Specify the log file
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Specify log message format
)


class CLevelOneEncryption:
    def __init__(self, level=1):
        xor_key_hex = os.getenv(f'XOR_KEY_LEVEL{level}', '')
        if xor_key_hex is None:
            raise ValueError(f'XOR key for level {level} not found in the environment.')

        self.__xor_key = bytes.fromhex(xor_key_hex)
        self.__caesar_shift = int(os.getenv('CAESAR_SHIFT', ''))
        self.__prefix = os.getenv('PREFIX', '')
        self.__suffix = os.getenv('SUFFIX', '')

    def encrypt(self, input_text):
        plain_text = self.__prefix + input_text + self.__suffix
        caesar_text = CaesarCipher.apply_caesar_shift(plain_text, self.__caesar_shift)
        encrypted_text = XORCipher.encrypt(caesar_text.encode('utf-8'), self.__xor_key)
        print("E_text1: ", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_bytes = XORCipher.decrypt(encrypted_text, self.__xor_key)
        caesar_text = decrypted_bytes.decode('utf-8')
        original_text = CaesarCipher.remove_caesar_shift(caesar_text, self.__caesar_shift)
        decrypted_text = original_text[len(self.__prefix):-len(self.__suffix)]
        print("D_text1: ", decrypted_text)
        return decrypted_text
