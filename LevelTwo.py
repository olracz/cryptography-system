import base64
class CLevelTwoEncryption:

    def __init__(self):
        self.__XOR_Key = 'Helloworld'

    def encrypt(self, encrypted_text):

        text_bytes = encrypted_text
        key_bytes = self.__XOR_Key.encode('utf-8')
        result = bytearray()

        for i, char in enumerate(encrypted_text):
            encrypted_byte = text_bytes[i] ^ key_bytes[i % len(key_bytes)]
            result.append(encrypted_byte)
        print("Not applied by b64: ", result)
        encoded_result = base64.b64encode(result)
        return encoded_result

    def decrypt(self, encrypted_text):
        decrypted_text = ""
        xor_key1 = self.__XOR_Key * len(encrypted_text)

        for i, char in enumerate(encrypted_text):
            c1 = chr(ord(char) ^ ord(xor_key1[i % len(xor_key1)]))
            decrypted_text += c1

        return decrypted_text


