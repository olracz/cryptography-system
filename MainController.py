import sys

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
            user_choices = input('what to do?:')
            if user_choices == '1':
                self.handle_user_choices(user_choices, level_one_encryption)
            elif user_choices == '2':
                self.handle_user_choices(user_choices, level_one_encryption)
            elif user_choices =='3':
                sys.exit()
            else:
                print("Please enter only from choices")
                print()

    def handle_user_choices(self, user_choices, level_one_encryption):
        while True:
            if user_choices == '1':
                self.__Text = input('Enter text to encrypt:')
                e_text = level_one_encryption.encrypt(self.__Text)
                break
            if user_choices == '2':
                self.__Text = input('Enter text to decrypt:')
                e_text = level_one_encryption.decrypt(self.__Text)





main_controller = CMainController()
main_controller.execute()
