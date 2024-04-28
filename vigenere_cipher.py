import feq_of_letters
import is_english_word
# make a vigenere cipher of the lowercase english alphabet only
# key is the key
# text is the text to be encrypted

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def vigenere_cipher(key, text):
    cipher_text = ''
    for i in range(len(text)):
        if text[i] in ALPHABET:
            p = ALPHABET.index(text[i])
            k = ALPHABET.index(key[i % len(key)])
            c = (p + k) % 26
            cipher_text += ALPHABET[c]
        else:
            # if the character is not in the alphabet, add it to the cipher text mostly for spaces
            cipher_text += text[i]
    return cipher_text


def decrypt_vigenere_cipher(key, text):
    plain_text = ''
    for i in range(len(text)):
        if text[i] in ALPHABET:
            c = ALPHABET.index(text[i])
            k = ALPHABET.index(key[i % len(key)])
            p = (c - k) % 26
            plain_text += ALPHABET[p]
        else:
            # if the character is not in the alphabet, add it to the plain text mostly for spaces
            plain_text += text[i]
    return plain_text


def vigenere_cipher_brute_force(text):
    filereader = open('dictionary.txt', 'r')
    dictionary = filereader.readlines()
    filereader.close()

    for word in dictionary:
        word = word.strip()
        word = word.lower()
        decrypted_wins = ''
        decrypted = decrypt_vigenere_cipher(word, text)
        if is_english_word.is_logically_english(decrypted, 0.60):
            decrypted_wins += decrypted
            print('Key: ' + word + ' Text: ' + decrypted_wins)
    return decrypted_wins


def vigenere_cipher_frequency_attack(L, text):
    return 0


def index_of_coincidence(text):
    frequency = [0]*26  # frequency of each letter in the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    for char in text:
        if char in alphabet:
            # increment the frequency of the letter
            frequency[alphabet.index(char)] += 1
            total += 1
    ic = 0
    numerator = 0
    for i in range(26):
        numerator += frequency[i] * (frequency[i] - 1)  # Sum the numerators
    if total > 1:  # Avoid division by zero
        ic = 26 * numerator / (total * (total - 1))
    return ic


def index_of_coincidence_period(text):
    found = False
    period = 0
    while not found:
        period += 1
        slices = [''] * period
        for i in range(len(text)):
            slices[i % period] += text[i]  # Split the text into slices
        sum = 0
        for i in range(period):
            # Sum the index of coincidences of each slice
            sum += index_of_coincidence(slices[i])
        index_of_coincidence_average = sum / period
        # If the average index of coincidence is greater than 1.6, the period is found
        if index_of_coincidence_average > 1.6:
            found = True
            return period


monogram = feq_of_letters.get_frequency()
text = 'hello world i am a crazy man that likes dogs and ice cream i also hate opening up about tax fraud'
key = 'key'
print(vigenere_cipher(key, text))
print(decrypt_vigenere_cipher(key, vigenere_cipher(key, text)))
print(index_of_coincidence(text))
print(index_of_coincidence_period(text))
print(vigenere_cipher_brute_force(vigenere_cipher(key, text)))
