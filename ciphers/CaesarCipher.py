
class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        cipher = ""
        try :
            for character in plain_text:
                if character == " ":
                    cipher += character
                else:
                    if character.isupper():
                        cipher += chr((ord(character) + self.key - 65) % 26 + 65)
                    else:
                        cipher += chr((ord(character) + self.key - 97) % 26 + 97)
        except Exception as e:
            raise Exception("Error while encrypting, please check your input : " + str(e))
        return cipher

    def decrypt(self, cipher_text):
        plain = ""
        try:
            for character in cipher_text:
                if character == " ":
                    plain += character
                else:
                    if character.isupper():
                        plain += chr((ord(character) - self.key - 65) % 26 + 65)
                    else:
                        plain += chr((ord(character) - self.key - 97) % 26 + 97)
        except Exception as e:
            raise Exception("Error while encrypting, please check your input : " + str(e))
        return plain
