
class CryptoResult:
    def __init__(self, plain_text, cipher_text):
        self.plain_text = plain_text
        self.cipher_text = cipher_text

    def json(self):
        return self.__dict__


class ErrorResult:
    def __init__(self, error):
        self.error = error

    def json(self):
        return self.__dict__
