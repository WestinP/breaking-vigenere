# make a vigenere cipher of the lowercase english alphabet only
# L is the length of the key
# key is the key
# text is the text to be encrypted

def vigenere_cipher(L, key, text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    text = text.lower()
    encrypted_text = ''
    for i in range(len(text)):
        if text[i] in alphabet:
            encrypted_text += alphabet[(alphabet.index(text[i]) +
                                        alphabet.index(key[i % L])) % 26]
        else:
            encrypted_text += text[i]
    return encrypted_text


def decrypt_vigenere_cipher(L, key, text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    text = text.lower()
    decrypted_text = ''
    for i in range(len(text)):
        if text[i] in alphabet:
            decrypted_text += alphabet[(alphabet.index(text[i]) -
                                        alphabet.index(key[i % L])) % 26]
        else:
            decrypted_text += text[i]
    return decrypted_text


def vigenere_cipher_frequency_attack(L, text):
    return 0


# Testing the function
L = 3
key = 'key'
text = 'hello worlD'
print(vigenere_cipher(L, key, text))  # prints 'rijvs gspvh'
print(decrypt_vigenere_cipher(L, key, 'rijvs gspvh'))  # prints 'hello world'
