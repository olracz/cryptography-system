class XORCipher:
    @staticmethod
    def encrypt(plaintext_bytes, xor_key):
        return bytearray(byte ^ xor_key[i % len(xor_key)] for i, byte in enumerate(plaintext_bytes))

    @staticmethod
    def decrypt(encrypted_bytes, xor_key):
        return bytearray(byte ^ xor_key[i % len(xor_key)] for i, byte in enumerate(encrypted_bytes))
