import sys
from bruteforce import dictionary_bruteforce, ioc_bruteforce
from vigenere import vigenere_encrypt
    
    
plaintext = 'The quick brown fox jumps over lazy dogs, navigating through thick jungles and murky swamps. Avid explorers, they search for hidden treasures, guided by ancient maps and cryptic clues. Their adventures take them across vast oceans and towering mountains, encountering perilous challenges and mysterious creatures. With courage and determination, they overcome obstacles, forging bonds of friendship and loyalty. Each step brings them closer to their goal, a legendary artifact of immense power and significance. Through trials and tribulations, they prove their worth and earn their place in history'


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <key> <ioc | dict>")
        print("Note: Plaintext is saved as a variable in `main.py`")
        sys.exit(1)
    
    key = sys.argv[1]
    attack_mode = sys.argv[2]

    ciphertext = vigenere_encrypt(key, plaintext)

    found_key = ''
    found_plaintext = ''

    if attack_mode == "ioc":
        (found_key, found_plaintext) = ioc_bruteforce(ciphertext, 0.003)
    elif attack_mode == "dict":
        (found_key, found_plaintext) = dictionary_bruteforce(ciphertext, 0.60)
    else:
        print("Invalid attack mode. Please choose 'ioc' or 'dict'")
        sys.exit(1)

    print(f"Found Key: {found_key}")
    print(f"Found Plaintext: {found_plaintext}")

    