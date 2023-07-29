import base64
import secrets
class CLevelFiveEncryption:

    def __init__(self, key_length=16):
        self.__XOR_Key = secrets.token_bytes(key_length)

    def encrypt(self, encrypted_text):

        result = bytearray()

        for i, char in enumerate(encrypted_text):
            encrypted_byte = encrypted_text[i] ^ self.__XOR_Key[i % len(self.__XOR_Key)]
            result.append(encrypted_byte)

        encoded_result = base64.b64encode(result).decode()
        print("level 5 encrypt: ", encoded_result)
        return encoded_result

    def decrypt(self, encrypted_text):

        decoded_bytes = base64.b64decode(encrypted_text)

        decrypted_bytes = bytearray()

        for i, byte in enumerate(decoded_bytes):
            decrypted_byte = byte ^ self.__XOR_Key[i % len(self.__XOR_Key)]
            decrypted_bytes.append(decrypted_byte)

        return decrypted_bytes
