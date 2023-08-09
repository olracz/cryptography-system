import sys

from generate_key_script import generate_and_store_keys

from LevelOne import CLevelOneEncryption
from LevelTwo import CLevelTwoEncryption
from LevelThree import CLevelThreeEncryption
from LevelFour import CLevelFourEncryption
from LevelFive import CLevelFiveEncryption


class CMainController:

    def __init__(self):
        self.__Text = ''

    def execute(self):
        level_one_encryption = CLevelOneEncryption()
        level_two_encryption = CLevelTwoEncryption()
        level_three_encryption = CLevelThreeEncryption()
        level_four_encryption = CLevelFourEncryption()
        level_five_encryption = CLevelFiveEncryption()

        while True:

            print('1.Encrypt')
            print('2.Decrypt')
            print('3.Exit')
            user_choices = input('what to do?:\n')
            if user_choices == '1':

                generate_and_store_keys()

                self.handle_user_choices(user_choices, level_one_encryption, level_two_encryption,
                                         level_three_encryption, level_four_encryption, level_five_encryption)
            elif user_choices == '2':
                self.handle_user_choices(user_choices, level_one_encryption, level_two_encryption,
                                         level_three_encryption, level_four_encryption, level_five_encryption)
            elif user_choices == '3':
                sys.exit()
            else:
                print("Please enter only from choices\n")

    def handle_user_choices(self, user_choices, level_one_encryption, level_two_encryption, level_three_encryption,
                            level_four_encryption, level_five_encryption):
        while True:
            if user_choices == '1':
                self.__Text = input('Enter text to encrypt:\n')
                if self.__Text == "":
                    continue
                e_text_one = level_one_encryption.encrypt(self.__Text)
                e_text_two = level_two_encryption.encrypt(e_text_one)
                e_text_three = level_three_encryption.encrypt(e_text_two)
                e_text_four = level_four_encryption.encrypt(e_text_three)
                e_text_five = level_five_encryption.encrypt(e_text_four)

                break

            if user_choices == '2':
                self.__Text = input('Enter text to decrypt:\n')
                if self.__Text == "":
                    continue
                e_text_five = level_five_encryption.decrypt(self.__Text)
                e_text_four = level_four_encryption.decrypt(e_text_five)
                e_text_three = level_three_encryption.decrypt(e_text_four)
                e_text_two = level_two_encryption.decrypt(e_text_three)
                e_text_one = level_one_encryption.decrypt(e_text_two)
                print("Decrypted output:\n", e_text_one)
                break


main_controller = CMainController()
main_controller.execute()
