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
text = 'The quick brown fox jumps over lazy dogs, navigating through thick jungles and murky swamps. Avid explorers, they search for hidden treasures, guided by ancient maps and cryptic clues. Their adventures take them across vast oceans and towering mountains, encountering perilous challenges and mysterious creatures. With courage and determination, they overcome obstacles, forging bonds of friendship and loyalty. Each step brings them closer to their goal, a legendary artifact of immense power and significance. Through trials and tribulations, they prove their worth and earn their place in history'
cipherText = vigenere_cipher(L, key, text)
print(cipherText)  # prints 'dlc ussgi fpyal jmh heqnc mfip pyjc nsec, xetskydmlq rrvmekf xfsgi nsxkjow krb qsbow wukqnc. kzgn chtjyvcbw, xfoc ciybgf jmb fshbor dvckwsbiq, eemboh lc krasild kktq eln abcndma gjeiq. rrigb ynzcxxsbiq xyui dlcw ymvmcw feqd mmiyxw krb xmgipsre qmerrkmlc, orayyldipsre tcbmjyyq gfkpjoreow krb qwcxcbmmew mvckxsbiq. usxf gmevyqi krb hcdipwmlkxgyr, xfoc yzcbgmwi yfqdeaviq, dyvesre fmxhq sd jpsilnwfst krb pmiejdc. iyml cxcz zbmlqw dlcw avsqov ds dlcsv qsyv, k jokcxhybc kvrsjymx yj sqkorqo nyacb yxh cmexmdsgyxgc. rrvmekf xpsejc yxh dvglyjkxgyrq, rriw tpyzc xfomp ambxf eln ckvl xfomp tjkgc ml lgcxmbc'
print(decrypt_vigenere_cipher(L, key, 'dlc ussgi fpyal jmh heqnc mfip pyjc nsec, xetskydmlq rrvmekf xfsgi nsxkjow krb qsbow wukqnc. kzgn chtjyvcbw, xfoc ciybgf jmb fshbor dvckwsbiq, eemboh lc krasild kktq eln abcndma gjeiq. rrigb ynzcxxsbiq xyui dlcw ymvmcw feqd mmiyxw krb xmgipsre qmerrkmlc, orayyldipsre tcbmjyyq gfkpjoreow krb qwcxcbmmew mvckxsbiq. usxf gmevyqi krb hcdipwmlkxgyr, xfoc yzcbgmwi yfqdeaviq, dyvesre fmxhq sd jpsilnwfst krb pmiejdc. iyml cxcz zbmlqw dlcw avsqov ds dlcsv qsyv, k jokcxhybc kvrsjymx yj sqkorqo nyacb yxh cmexmdsgyxgc. rrvmekf xpsejc yxh dvglyjkxgyrq, rriw tpyzc xfomp ambxf eln ckvl xfomp tjkgc ml lgcxmbc'))  # prints 'The quick brown fox jumps over lazy dogs, navigating through thick jungles and murky swamps. Avid explorers, they search for hidden treasures, guided by ancient maps and cryptic clues. Their adventures take them across vast oceans and towering mountains, encountering perilous challenges and mysterious creatures. With courage and determination, they overcome obstacles, forging bonds of friendship and loyalty. Each step brings them closer to their goal, a legendary artifact of immense power and significance. Through trials and tribulations, they prove their worth and earn their place in history'

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


iocPeriod = index_of_coincidence_period(cipherText)
print(index_of_coincidence(cipherText)) # p
print(index_of_coincidence_period(cipherText)) #Should return 3

"""# Fitness
How closely a piece of text resembles the english language

"""

# Expected letter frequencies in English text (approximate values)
english_freq = {
        'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425,
        'e': 0.1270, 'f': 0.0223, 'g': 0.0202, 'h': 0.0609,
        'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
        'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193,
        'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
        'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
        'y': 0.0197, 'z': 0.0007
    }

import re
from collections import Counter

def fitness (text):
  cleaned_text = re.sub(r'[^a-zA-Z]', '', text.lower())
  letter_freq = Counter(text)
  fitness = sum((letter_freq.get(letter, 0) / len(cleaned_text) - freq) ** 2
                  for letter, freq in english_freq.items())
  threshold = 0.007
  return fitness < threshold


"""# Brute Force Approach
if you know the key length (uses Ioc_period)
"""
def bruteForce(ioc_period, cipher_text):
  unknownKey = [''] * ioc_period
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for unknownKey[0] in alphabet:
      for unknownKey[1] in alphabet:
        for unknownKey[2] in alphabet:
          pt = decrypt_vigenere_cipher(ioc_period, ''.join(unknownKey), cipher_text)
          fit = fitness(pt)
          if fit:
            break
        else:
          continue
        break
      else:
        continue
      break
  plaintext = decrypt_vigenere_cipher(ioc_period, ''.join(unknownKey), cipher_text)
  return plaintext

#testing bruteForce
print(bruteForce(iocPeriod, cipherText))
