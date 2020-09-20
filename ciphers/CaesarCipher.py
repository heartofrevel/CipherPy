class CaesarCipher:
    def __init__(self, key, preserve_spaces=False):
        self.key = key
        self.preserve_spaces = preserve_spaces

    def encrypt(self, plain_text):
        try:
            if self.preserve_spaces:
                cipher = ''.join(chr((ord(char) + self.key - 65) % 26 + 65) if char.isupper() else chr(
                    (ord(char) + self.key - 97) % 26 + 97) if char.islower() else ' ' for char in plain_text)
            else:
                cipher = ''.join(chr((ord(char) + self.key - 65) % 26 + 65) if char.isupper() else chr(
                    (ord(char) + self.key - 97) % 26 + 97) for char in plain_text.replace(' ', ''))
        except Exception as e:
            raise Exception("Error while encrypting, please check your input : " + str(e))
        return cipher

    def decrypt(self, cipher_text):
        try:
            if self.preserve_spaces:
                plain = ''.join(chr((ord(char) - self.key - 65) % 26 + 65) if char.isupper() else chr(
                    (ord(char) - self.key - 97) % 26 + 97) if char.islower() else ' ' for char in cipher_text)
            else:
                plain = ''.join(chr((ord(char) - self.key - 65) % 26 + 65) if char.isupper() else chr(
                    (ord(char) - self.key - 97) % 26 + 97) for char in cipher_text.replace(' ', ''))
        except Exception as e:
            raise Exception("Error while encrypting, please check your input : " + str(e))
        return plain
