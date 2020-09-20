from util import CipherUtil


class AffineCipher:
    def __init__(self, k1, k2, preserve_spaces=False):
        self.k1 = k1
        self.k2 = k2
        self.preserve_spaces = preserve_spaces
        self.alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
                         "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
                         "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
        if self.k1 > len(self.alphabet) or self.k2 > len(self.alphabet):
            raise Exception("Keys cannot be greater than alphabet length : " + str(len(self.alphabet)))

        result_gcd = CipherUtil.gcd(self.k1, len(self.alphabet))

        if result_gcd > 1:
            raise Exception("Key key1 has common factors apart from 1 with length of alphabet : "
                            + str(str(len(self.alphabet)))+ ". Possible values are 1,3,5,7,9,11,15,17,19,21,23,25")

        self.alphabet_reverse = {v: k for k, v in self.alphabet.items()}

    def encrypt(self, plain_text):
        try:
            if self.preserve_spaces:
                result = ''.join(self.alphabet_reverse[((self.k1 * self.alphabet[char]) + self.k2) %
                                                       len(self.alphabet)] if char != ' ' else ' ' for char in plain_text.upper())
            else:
                result = ''.join(self.alphabet_reverse[((self.k1 * self.alphabet[char]) + self.k2) %
                                                       len(self.alphabet)] for char in plain_text.upper().replace(' ', ''))
        except Exception as e:
            raise Exception("Error while encrypting, please check your input. Unknown character : " + str(e))
        return result

    def decrypt(self, cipher_text):
        try:
            inverse_key1 = CipherUtil.inv(self.k1, len(self.alphabet))
            if self.preserve_spaces:
                result = ''.join(
                    self.alphabet_reverse[(inverse_key1 * (self.alphabet[char] - self.k2))
                                          % len(self.alphabet)] if char != ' ' else ' ' for char in cipher_text.upper())
            else:
                result = ''.join(
                    self.alphabet_reverse[(inverse_key1 * (self.alphabet[char] - self.k2))
                                          % len(self.alphabet)] for char in cipher_text.upper().replace(' ', ''))
        except Exception as e:
            raise Exception("Error while decrypting, please check your input. Unknown character : " + str(e))
        return result

