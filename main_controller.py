from generate_key_script import generate_and_store_keys
from level_one import CLevelOneEncryption
from encryption_levels import BaseEncryption
from level_eight import CLevelEightEncryption
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


class CMainController:
    def __init__(self):
        self.level_one_encryption = CLevelOneEncryption()
        self.encryption_levels = [BaseEncryption(level=i) for i in range(2, 8)]
        self.level_eight_encryption = CLevelEightEncryption()

        generate_and_store_keys()

    def encrypt(self, text):
        logging.debug("Text : %s", text)
        encrypted_text = self.level_one_encryption.encrypt(text)
        for encryption_level in self.encryption_levels:
            encrypted_text = encryption_level.encrypt(encrypted_text)
        encrypted_text = self.level_eight_encryption.encrypt(encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = self.level_eight_encryption.decrypt(encrypted_text)
        for encryption_level in reversed(self.encryption_levels):
            decrypted_text = encryption_level.decrypt(decrypted_text)
        decrypted_text = self.level_one_encryption.decrypt(decrypted_text)
        generate_and_store_keys()
        return decrypted_text


main_controller = CMainController()
