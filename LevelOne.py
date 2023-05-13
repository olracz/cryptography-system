class CLevelOneEncryption:

    def __init__(self):
        self.__Plain_text = ''
        self.__Prefix = 'Carlo'
        self.__Suffix = 'Cobey'
        self.__XOR_Key = 'L'
        self.__Caesar_shift = 5

    def encrypt(self, input_text):
        self.__Plain_text = self.__Prefix + input_text + self.__Suffix
        caesar_text = ""
        result = []
        # Perform caesar cipher first
        for char in self.__Plain_text:
            caesar_text += chr((ord(char) + self.__Caesar_shift))  # plus 5 shift

        xor_key = self.__XOR_Key * len(caesar_text)

        for i, char in enumerate(caesar_text):
            print(xor_key[i & len(xor_key)])
            c1 = chr(char ^ ord(xor_key[i & len(xor_key)]))
            result += c1
        return result

    def decrypt(self, input_text):
        decrypted_xor = ""
        decrypted_caesar = ""

        for i, c in enumerate(input_text):
            c1 = chr(ord(c) ^ ord(self.__XOR_Key[i % len(self.__XOR_Key)]))
            decrypted_xor += c1

        for char in decrypted_xor:
            decrypted_caesar = chr(ord(char) - self.__Caesar_shift)

        return decrypted_caesar





