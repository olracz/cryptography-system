import os
from dotenv import load_dotenv

load_dotenv()
class CLevelOneEncryption:
    def __init__(self):
        self.__Plain_text = ''
        self.__Prefix = os.getenv('PREFIX')
        self.__Suffix = os.getenv('SUFFIX')
        self.__XOR_Key = os.getenv('XOR_KEY_LEVEL1')
        self.__Caesar_shift: int = int(os.getenv('CAESAR_SHIFT'))

    def encrypt(self, input_text):
        self.__Plain_text = self.__Prefix + input_text + self.__Suffix

        caesar_text = ""
        result = bytearray()

        for char in self.__Plain_text:
            caesar_text += chr((ord(char) + self.__Caesar_shift) % 256)

        text_bytes = caesar_text.encode('utf-8')
        key_bytes = self.__XOR_Key.encode('utf-8')

        for i, char in enumerate(caesar_text):
            encrypted_byte = text_bytes[i] ^ key_bytes[i % len(key_bytes)]
            result.append(encrypted_byte)

        return result
    def decrypt(self, encrypted_text):

        caesar_text = ""
        key_bytes = self.__XOR_Key.encode('utf-8')

        for i, byte in enumerate(encrypted_text):
            decrypted_byte = byte ^ key_bytes[i % len(key_bytes)]
            caesar_text += chr(decrypted_byte)

        original_text = ""

        for char in caesar_text:
            original_text += chr((ord(char) - self.__Caesar_shift) % 256)

        decrypted_text = original_text[len(self.__Prefix):-len(self.__Suffix)]
        print("Decrypted text: ", decrypted_text)
        return decrypted_text
