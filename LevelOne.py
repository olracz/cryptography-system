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
        result = []
        for i, c in enumerate(caesar_text):
            test1 = i & len(xor_key)
            test2 = xor_key[i & len(xor_key)]
            test = ord(xor_key[i & len(xor_key)])
            c1 = chr(ord(c) ^ ord(xor_key[i & len(xor_key)]))
            result.append(c1)
        return "".join(result)



    #def decrypt(self, input_text):