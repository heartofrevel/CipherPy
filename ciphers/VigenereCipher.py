class VigenereCipher:
    def __init__(self, key, message, preserve_spaces=False):
        self.preserve_spaces = preserve_spaces
        if self.preserve_spaces:
            self.message = message
        else:
            self.message = message.replace(' ', '')

        if len(self.message) == len(key):
            pass
        else:
            count = 0
            self.key = []
            for i in range(len(self.message)):
                if self.message[i] != ' ':
                    self.key.append(key[count % len(key)])
                    count += 1
                else:
                    self.key.append(' ')

    def encrypt(self):
        try:
            cipher = "".join(
                chr((ord(self.message[i]) + ord(self.key[i])) % 26 + ord('A')) if self.message[i] != ' ' else ' ' for i
                in range(len(self.message)))
        except Exception as e:
            raise Exception("Error while encrypting, please check your input : " + str(e))
        return cipher

    def decrypt(self):
        try:
            plain = "".join(
                chr((ord(self.message[i]) - ord(self.key[i])) % 26 + ord('A')) if self.message[i] != ' ' else ' ' for i
                in range(len(self.message)))
        except Exception as e:
            raise Exception("Error while decrypting, please check your input : " + str(e))
        return plain
