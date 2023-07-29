import secrets
class CLevelOneEncryption:
    def __init__(self, key_length=32):
        self.__Plain_text = ''
        self.__Prefix = secrets.token_hex(16)
        self.__Suffix = secrets.token_hex(16)
        self.__XOR_Key = secrets.token_bytes(key_length)
        self.__Caesar_shift = secrets.randbelow(256) + 1

    def encrypt(self, input_text):
        self.__Plain_text = self.__Prefix + input_text + self.__Suffix

        caesar_text = ""
        result = bytearray()

        for char in self.__Plain_text:
            caesar_text += chr((ord(char) + self.__Caesar_shift) % 256)

        text_bytes = caesar_text.encode('utf-8')

        for i, char in enumerate(caesar_text):
            encrypted_byte = text_bytes[i] ^ self.__XOR_Key[i % len(self.__XOR_Key)]
            result.append(encrypted_byte)
        print("level 1 encrypt: ", result)
        return result
    def decrypt(self, encrypted_text):

        caesar_text = ""

        for i, byte in enumerate(encrypted_text):
            decrypted_byte = byte ^ self.__XOR_Key[i % len(self.__XOR_Key)]
            caesar_text += chr(decrypted_byte)

        original_text = ""

        for char in caesar_text:
            original_text += chr((ord(char) - self.__Caesar_shift) % 256)

        decrypted_text = original_text[len(self.__Prefix):-len(self.__Suffix)]
        return decrypted_text
