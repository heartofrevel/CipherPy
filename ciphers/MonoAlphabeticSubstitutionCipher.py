
class MonoAlphabeticSubstitutionCipher:
    def __init__(self, key_pt, key_ct):
        self.key_pt = key_pt
        self.key_ct = key_ct
        if len(key_ct) != len(key_pt):
            raise Exception("Plain Text key and Cipher Text key lengths are not same")

    def encrypt(self, plain_text):
        key_dict = {self.key_pt[i]: self.key_ct[i] for i in range(len(self.key_pt))}
        result = ''
        try:
            result = ''.join(key_dict[char] for char in plain_text)
        except Exception as e:
            raise Exception("Error while encrypting, please check your input. Unknown character : "+str(e))
        return result

    def decrypt(self, cipher_text):
        key_dict = {self.key_ct[i]: self.key_pt[i] for i in range(len(self.key_pt))}
        result = ''
        try:
            result = ''.join(key_dict[char] for char in cipher_text)
        except Exception as e:
            raise Exception("Error while decrypting, please check your input. Unknown character : "+str(e))
        return result
