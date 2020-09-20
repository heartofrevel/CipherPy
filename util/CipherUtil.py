def gcd(key, alphabet_length):
    return key if not alphabet_length else gcd(alphabet_length, key % alphabet_length)


def inv(key, alphabet_length):
    for num in range(1, alphabet_length):
        if (key * num) % alphabet_length == 1:
            return num

