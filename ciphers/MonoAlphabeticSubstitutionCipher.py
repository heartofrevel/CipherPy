class MonoAlphabeticSubstitutionCipher:
    def __init__(self, key_pt, key_ct, preserve_spaces=False):
        self.key_pt = key_pt
        self.key_ct = key_ct
        self.preserve_spaces = preserve_spaces
        if len(key_ct) != len(key_pt):
            raise Exception("Plain Text key and Cipher Text key lengths are not same")

    def encrypt(self, plain_text):
        key_dict = {self.key_pt[i]: self.key_ct[i] for i in range(len(self.key_pt))}
        try:
            if self.preserve_spaces:
                result = ''.join(key_dict[char] if char != ' ' else ' ' for char in plain_text)
            else:
                result = ''.join(key_dict[char] for char in plain_text.replace(' ', ''))
        except Exception as e:
            raise Exception("Error while encrypting, please check your input. Unknown character : "+str(e))
        return result

    def decrypt(self, cipher_text):
        key_dict = {self.key_ct[i]: self.key_pt[i] for i in range(len(self.key_pt))}
        try:
            if self.preserve_spaces:
                result = ''.join(key_dict[char] if char != ' ' else ' ' for char in cipher_text)
            else:
                result = ''.join(key_dict[char] for char in cipher_text.replace(' ', ''))
        except Exception as e:
            raise Exception("Error while decrypting, please check your input. Unknown character : "+str(e))
        return result
