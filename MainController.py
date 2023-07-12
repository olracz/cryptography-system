import sys
import base64
from LevelOne import CLevelOneEncryption


class CMainController:
    def __init__(self):
        self.__Text = ''

    def execute(self):
        level_one_encryption = CLevelOneEncryption()
        while True:
            print('1.Encrypt')
            print('2.Decrypt')
            print('3.Exit')
            user_choices = input('what to do?:\n')
            if user_choices == '1':
                self.handle_user_choices(user_choices, level_one_encryption)
            elif user_choices == '2':
                self.handle_user_choices(user_choices, level_one_encryption)
            elif user_choices == '3':
                sys.exit()
            else:
                print("Please enter only from choices\n")

    def handle_user_choices(self, user_choices, level_one_encryption):
        while True:
            if user_choices == '1':
                self.__Text = input('Enter text to encrypt:\n')
                if self.__Text == "":
                    continue
                e_text = level_one_encryption.encrypt(self.__Text)
                binary_format = e_text.encode('utf-8')
                binary = ' '.join(format(byte, '08b')for byte in binary_format)
                encode = base64.b64encode(binary_format).decode()
                print("Encrypted output:\n", e_text)
                print("Encrypted output binary:\n", binary)
                print("Base64 encoded output:\n", encode)
                break
            if user_choices == '2':
                self.__Text = input('Enter text to decrypt:\n')
                if self.__Text == "":
                    continue
                e_text = level_one_encryption.decrypt(self.__Text)
                print("Decrypted output:\n", e_text)
                break


main_controller = CMainController()
main_controller.execute()
