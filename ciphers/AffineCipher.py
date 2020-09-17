class AffineCipher:
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2
        self.alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
                        "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
                        "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, " ": 26}
        if self.k1 > len(self.alphabet) or self.k2 > len(self.alphabet):
            raise Exception("Keys cannot be greater than alphabet length : " + str(len(self.alphabet)))

        result_gcd = AffineCipher.gcd(self.k1, len(self.alphabet))

        if result_gcd > 1:
            raise Exception("Key key1 has common factors apart from 1 with length of alphabet : "
                            + str(str(len(self.alphabet))))

        self.alphabet_reverse = {v: k for k, v in self.alphabet.items()}

    def encrypt(self, plain_text):
        try:
            result = ''.join(self.alphabet_reverse[((self.k1 * self.alphabet[char]) + self.k2) %
                                                   len(self.alphabet)] for char in plain_text.upper())
        except Exception as e:
            raise Exception("Error while encrypting, please check your input. Unknown character : "+str(e))
        return result

    def decrypt(self, cipher_text):
        try:
            inverse_key1 = AffineCipher.inv(self.k1, len(self.alphabet))
            result = ''.join(self.alphabet_reverse[(inverse_key1*(self.alphabet[char] - self.k2)) % len(self.alphabet)] for char in cipher_text.upper())
        except Exception as e:
            raise Exception("Error while encrypting, please check your input. Unknown character : " + str(e))
        return result

    @staticmethod
    def gcd(key, alphabet_length):
        return key if not alphabet_length else AffineCipher.gcd(alphabet_length, key % alphabet_length)

    @staticmethod
    def inv(key, alphabet_length):
        for num in range(1, alphabet_length):
            if (key*num) % alphabet_length == 1:
                return num




