import secrets
class CLevelThreeEncryption:

    def __init__(self, key_length=16):
        self.__XOR_Key: bytes = secrets.token_bytes(key_length)

    def encrypt(self, encrypted_text):

        result = bytearray()

        for i, char in enumerate(encrypted_text):
            encrypted_byte = encrypted_text[i] ^ self.__XOR_Key[i % len(self.__XOR_Key)]
            result.append(encrypted_byte)
        print("level 3 encrypt: ", result)

        return result

    def decrypt(self, encrypted_text):

        decrypted_bytes = bytearray()

        for i, byte in enumerate(encrypted_text):
            decrypted_byte = byte ^ self.__XOR_Key[i % len(self.__XOR_Key)]
            decrypted_bytes.append(decrypted_byte)

        return decrypted_bytes
