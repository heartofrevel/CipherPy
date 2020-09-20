class AtbashCipher:
    def __init__(self, preserve_spaces=False):
        self.key_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
                          'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
                          'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
                          'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
                          'Y': 'B', 'Z': 'A'}
        self.preserve_spaces = preserve_spaces

    def encrypt(self, plain_text):
        try:
            if self.preserve_spaces:
                cipher = "".join(self.key_table[char] if char != ' ' else ' ' for char in plain_text.upper())
            else:
                cipher = "".join(self.key_table[char] for char in plain_text.upper().replace(' ', ''))
        except Exception as e:
            raise Exception("Error while encrypting, please check your input : " + str(e))
        return cipher

    def decrypt(self, cipher_text):
        try:
            if self.preserve_spaces:
                plain = "".join(self.key_table[char] if char != ' ' else ' ' for char in cipher_text.upper())
            else:
                plain = "".join(self.key_table[char] for char in cipher_text.upper().replace(' ', ''))
        except Exception as e:
            raise Exception("Error while decrypting, please check your input : " + str(e))
        return plain
