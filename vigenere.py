ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def vigenere_encrypt(key: str, plain: str) -> str:
    key = key.lower()
    plain = plain.lower()
    cipher_text = ''
    for i in range(len(plain)):
        if plain[i] in ALPHABET:
            cipher_text += ALPHABET[(ALPHABET.index(plain[i]) +
                                        ALPHABET.index(key[i % len(key)])) % 26]
        else:
            cipher_text += plain[i]
    return cipher_text


def vigenere_decrypt(key: str, cipher: str) -> str:
    key = key.lower()
    cipher = cipher.lower()
    cipher_text = ''
    for i in range(len(cipher)):
        if cipher[i] in ALPHABET:
            cipher_text += ALPHABET[(ALPHABET.index(cipher[i]) -
                                        ALPHABET.index(key[i % len(key)])) % 26]
        else:
            cipher_text += cipher[i]
    return cipher_text