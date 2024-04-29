from index_of_coincidence import ioc_period
from is_english_word import is_logically_english, fitness
from vigenere import vigenere_decrypt
from itertools import product

# text = 'The quick brown fox jumps over lazy dogs, navigating through thick jungles and murky swamps. Avid explorers, they search for hidden treasures, guided by ancient maps and cryptic clues. Their adventures take them across vast oceans and towering mountains, encountering perilous challenges and mysterious creatures. With courage and determination, they overcome obstacles, forging bonds of friendship and loyalty. Each step brings them closer to their goal, a legendary artifact of immense power and significance. Through trials and tribulations, they prove their worth and earn their place in history'

"""
# Dictionary Brute Force Approach (Westin)
brute force dictionary attack

Returns (key, plaintext)
"""
def dictionary_bruteforce(cipher_text: str, english_percent=0.60):
    filereader = open('dictionary.txt', 'r')
    dictionary = filereader.readlines()
    filereader.close()

    for word in dictionary:
        word = word.strip()
        word = word.lower()
        decrypted = vigenere_decrypt(word, cipher_text)
        if is_logically_english(decrypted, english_percent):
            return (word, decrypted)
        
    return ('', '')

"""
# IOC Brute Force Approach (Anna)
if you know the key length (uses ioc_period to get potential key length) 

Returns (key, plaintext)
"""
def ioc_bruteforce(cipher_text: str, fitness_threshold=0.007):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    key_length = ioc_period(cipher_text)

    if key_length is None or key_length <= 0:
        print("No IOC found")
        return ('', '')

    # if key length is too long, warn about potentially long runtime
    # Test (uncomment to test key length )
    #print(f"IOC key length at {key_length}")
    if key_length > 6:
        print(f"Warning: IOC key length at {key_length}")

    for item in product(alphabet, repeat=key_length):
        potential_key = ''.join(item)
        pt = vigenere_decrypt(potential_key, cipher_text)
        fit = fitness(pt, fitness_threshold)
        if fit:
            return (potential_key, vigenere_decrypt(potential_key, cipher_text))
        
    return ('', '')
