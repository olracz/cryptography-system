
import ast
class CLevelOneEncryption:


        def __init__(self):
            self.__Plain_text = ''
            self.__Prefix = 'Kaido'
            self.__Suffix = 'Blackbeard'
            self.__XOR_Key = 'L'
            self.__Caesar_shift = 5

        def encrypt(self, input_text):
            self.__Plain_text = self.__Prefix + input_text + self.__Suffix
            print()
            print("Step 1: Appending prefix and suffix to input text")
            print("Modified input text :", self.__Plain_text)
            print()
            caesar_text = ""
            result = []

            for char in self.__Plain_text:
                caesar_text += chr((ord(char) + self.__Caesar_shift) % 256)
            print("Step 2: Performing Caesar encryption")
            print("Caesar encrypted text: ", caesar_text)
            print()

            xor_key = self.__XOR_Key * len(caesar_text)

            for i, char in enumerate(caesar_text):
                c1 = chr((ord(char) ^ ord(xor_key[i & len(xor_key)])))
                result += c1

            print("Step3 : Performing XOR encryption with key")
            print("Final encrpted text: ", result)
            

        def decrypt(self, input_text):

            user_list = ast.literal_eval(input_text)
            xor_key1 = self.__XOR_Key * len(user_list)
            caesar_text = ""

            for i, char in enumerate(user_list):
                c1 = chr(ord(char) ^ ord(xor_key1[i % len(xor_key1)]))
                caesar_text += c1
            print()
            print("Step 1 : Returning the value of caesar text before the xor cipher")
            print("Caesar text : " , caesar_text)
            print()

            original_text = ""

            for char in caesar_text:
                original_text += chr((ord(char) - self.__Caesar_shift) % 256)
            print("Step 2: Returning the value of plain text before caesar cipher")
            print("Plaintext: ", original_text)
            print()

            decrypted_text = original_text[len(self.__Prefix):-len(self.__Suffix)]
            print("Step 3 : Removing the prefix and suffix from plain text")
            print("Original text: ", decrypted_text)
            print()
            return decrypted_text
