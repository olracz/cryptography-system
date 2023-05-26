class CLevelOneEncryption:
    def __init__(self):
        self.__Plain_text = ''
        self.__Prefix = 'Kai-do'
        self.__Suffix = 'Blackbeard'
        self.__XOR_Key = 'L'
        self.__Caesar_shift = 5

    def encrypt(self, input_text):
        self.__Plain_text = self.__Prefix + input_text + self.__Suffix

        caesar_text = ""
        result = ""

        for char in self.__Plain_text:
            caesar_text += chr((ord(char) + self.__Caesar_shift) % 256)

        xor_key = self.__XOR_Key * len(caesar_text)

        for i, char in enumerate(caesar_text):
            c1 = chr((ord(char) ^ ord(xor_key[i & len(xor_key)])))
            result += c1
        return result

    def decrypt(self, input_text):
        xor_key1 = self.__XOR_Key * len(input_text)
        caesar_text = ""

        for i, char in enumerate(input_text):
            c1 = chr(ord(char) ^ ord(xor_key1[i % len(xor_key1)]))
            caesar_text += c1

        original_text = ""

        for char in caesar_text:
            original_text += chr((ord(char) - self.__Caesar_shift) % 256)

        decrypted_text = original_text[len(self.__Prefix):-len(self.__Suffix)]
        return decrypted_text
