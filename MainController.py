from generate_key_script import generate_and_store_keys
from LevelOne import CLevelOneEncryption
from LevelTwo import CLevelTwoEncryption
from LevelThree import CLevelThreeEncryption
from LevelFour import CLevelFourEncryption
from LevelFive import CLevelFiveEncryption
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


class CMainController:
    def __init__(self):
        self.level_one_encryption = CLevelOneEncryption()
        self.level_two_encryption = CLevelTwoEncryption()
        self.level_three_encryption = CLevelThreeEncryption()
        self.level_four_encryption = CLevelFourEncryption()
        self.level_five_encryption = CLevelFiveEncryption()

        generate_and_store_keys()

    def encrypt(self, text):
        logging.debug("Text : %s", text)
        e_text_one = self.level_one_encryption.encrypt(text)
        e_text_two = self.level_two_encryption.encrypt(e_text_one)
        e_text_three = self.level_three_encryption.encrypt(e_text_two)
        e_text_four = self.level_four_encryption.encrypt(e_text_three)
        e_text_five = self.level_five_encryption.encrypt(e_text_four)
        return e_text_five

    def decrypt(self, encrypted_text):
        e_text_five = self.level_five_encryption.decrypt(encrypted_text)
        e_text_four = self.level_four_encryption.decrypt(e_text_five)
        e_text_three = self.level_three_encryption.decrypt(e_text_four)
        e_text_two = self.level_two_encryption.decrypt(e_text_three)
        e_text_one = self.level_one_encryption.decrypt(e_text_two)
        return e_text_one


main_controller = CMainController()

