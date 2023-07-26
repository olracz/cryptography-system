import base64
class CLevelFiveEncryption:

    def __init__(self):
        self.__XOR_Key = 'Helloworld'

    def encrypt(self, encrypted_text):
        key_bytes = self.__XOR_Key.encode('utf-8')
        result = bytearray()

        for i, char in enumerate(encrypted_text):
            encrypted_byte = encrypted_text[i] ^ key_bytes[i % len(key_bytes)]
            result.append(encrypted_byte)

        encoded_result = base64.b64encode(result).decode()
        return encoded_result

    def decrypt(self, encrypted_text):

        decoded_bytes = base64.b64decode(encrypted_text)

        key_bytes = self.__XOR_Key.encode('utf-8')
        decrypted_bytes = bytearray()

        for i, byte in enumerate(decoded_bytes):
            decrypted_byte = byte ^ key_bytes[i % len(key_bytes)]
            decrypted_bytes.append(decrypted_byte)

        return decrypted_bytes
