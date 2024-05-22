from generate_key_script import generate_and_store_keys
from LevelOne import CLevelOneEncryption
from LevelTwo import CLevelTwoEncryption
from LevelThree import CLevelThreeEncryption
from LevelFour import CLevelFourEncryption
from LevelFive import CLevelFiveEncryption
from LevelSix import CLevelSixEncryption
from LevelSeven import CLevelSevenEncryption
from LevelEight import CLevelEightEncryption
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


class CMainController:
    def __init__(self):
        self.level_one_encryption = CLevelOneEncryption()
        self.level_two_encryption = CLevelTwoEncryption()
        self.level_three_encryption = CLevelThreeEncryption()
        self.level_four_encryption = CLevelFourEncryption()
        self.level_five_encryption = CLevelFiveEncryption()
        self.level_six_encryption = CLevelSixEncryption()
        self.level_seven_encryption = CLevelSevenEncryption()
        self.level_eight_encryption = CLevelEightEncryption()

        generate_and_store_keys()

    def encrypt(self, text):
        logging.debug("Text : %s", text)
        e_text_one = self.level_one_encryption.encrypt(text)
        e_text_two = self.level_two_encryption.encrypt(e_text_one)
        e_text_three = self.level_three_encryption.encrypt(e_text_two)
        e_text_four = self.level_four_encryption.encrypt(e_text_three)
        e_text_five = self.level_five_encryption.encrypt(e_text_four)
        e_text_six = self.level_six_encryption.encrypt(e_text_five)
        e_text_seven = self.level_seven_encryption.encrypt(e_text_six)
        e_text_eight = self.level_eight_encryption.encrypt(e_text_seven)
        return e_text_eight

    def decrypt(self, encrypted_text):
        d_text_eight = self.level_eight_encryption.decrypt(encrypted_text)
        d_text_seven = self.level_seven_encryption.decrypt(d_text_eight)
        d_text_six = self.level_six_encryption.decrypt(d_text_seven)
        d_text_five = self.level_five_encryption.decrypt(d_text_six)
        d_text_four = self.level_four_encryption.decrypt(d_text_five)
        d_text_three = self.level_three_encryption.decrypt(d_text_four)
        d_text_two = self.level_two_encryption.decrypt(d_text_three)
        d_text_one = self.level_one_encryption.decrypt(d_text_two)
        generate_and_store_keys()
        return d_text_one


main_controller = CMainController()
