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
        for i in range(len(self.__Plain_text)):
            char = self.__Plain_text[i]
            # Encrypt uppercase characters
            if char.isupper():
                caesar_text += chr((ord(char) + self.__Caesar_shift - 65) % 26 + 65)  # plus 5 shift
            # Encrypt lowercase characters
            elif char.islower():
                caesar_text += chr((ord(char) + self.__Caesar_shift - 97) % 26 + 97)
            # Encrypt non alphabet characters
            else:
                caesar_text += chr((ord(char) + self.__Caesar_shift) % 128)

        xor_key = self.__XOR_Key * len(caesar_text)

        for i, c in enumerate(caesar_text):
            test1 = i & len(xor_key)
            test2 = xor_key[i & len(xor_key)]
            test = ord(xor_key[i & len(xor_key)])
            c1 = chr(ord(c) ^ ord(xor_key[i & len(xor_key)]))
            result += c1
        return result

    def decrypt(self, input_text):
        decrypted_xor = ""
        decrypted_text = ""

        for i, c in enumerate(input_text):
            c1 = chr(ord(c) ^ ord(self.__XOR_Key[i % len(self.__XOR_Key)]))
            decrypted_xor += c1

        for char in decrypted_xor:
            if char.isupper():
                decrypted_caesar = chr((ord(char) -  self.__Caesar_shift - 65) % 26 + 65)
            # Encrypt lowercase characters
            elif char.islower():
                decrypted_caesar = chr((ord(char) - self.__Caesar_shift - 97) % 26 + 97)
            # Encrypt non alphabet characters
            else:
                decrypted_caesar = chr((ord(char) - self.__Caesar_shift) % 128)

            decrypted_text += decrypted_caesar

        return decrypted_text





