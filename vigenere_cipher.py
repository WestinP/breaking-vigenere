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

def index_of_coincidence(text):
    frequency = [0]*26 # frequency of each letter in the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    for char in text:
        if char in alphabet:
            frequency[alphabet.index(char)] += 1 # increment the frequency of the letter
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
            slices[i % period] += text[i] # Split the text into slices
        sum = 0
        for i in range(period):
            sum += index_of_coincidence(slices[i]) # Sum the index of coincidences of each slice
        index_of_coincidence_average = sum / period 
        if index_of_coincidence_average > 1.6: # If the average index of coincidence is greater than 1.6, the period is found
            found = True
            return period

# Testing the function
L = 3
key = 'key'
#changed the text to be longer since the index of coincidence is more accurate with a larger text than a short one
text = 'hello world i am westin pellicer and i am a student at the university of embry riddle i like fortnite and travvy patty mealz'
cipherText = vigenere_cipher(L, key, text)
iocPeriod = index_of_coincidence_period(cipherText)
print(cipherText)  # prints 'rijvs gspvh'
print(decrypt_vigenere_cipher(L, key, cipherText))  # prints 'hello world' decrypted from cipherText
print(index_of_coincidence(cipherText)) # should return a number greater than 1.6
print(index_of_coincidence_period(cipherText)) #Should return 3
