class CaesarCipher:
    @staticmethod
    def apply_caesar_shift(text, shift):
        return "".join(chr((ord(char) - 32 + shift) % 96 + 32) for char in text)

    @staticmethod
    def remove_caesar_shift(text, shift):
        return CaesarCipher.apply_caesar_shift(text, -shift)