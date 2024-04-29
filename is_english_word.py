import re
from collections import Counter


'''
Dictionary-based Fitness Function
'''

filereader = open('dictionary.txt', 'r')
dictionary = filereader.readlines()
filereader.close()

real_words = {}

for word in dictionary:
    word = word.strip()
    word = word.lower()
    real_words[word] = 1

def is_logically_english(text: str, percent: float) -> bool:
    maybe_words = text.split()
    if len(maybe_words) == 0:
        return False

    count = 0
    for word in maybe_words:
        if word in real_words:
            count += 1
    if count / len(maybe_words) >= percent:
        return True
    return False


'''
Frequency-Based Fitness Function
'''
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

def fitness (text, fitness_threshold):
  cleaned_text = re.sub(r'[^a-zA-Z]', '', text.lower())
  letter_freq = Counter(text)
  fitness = sum((letter_freq.get(letter, 0) / len(cleaned_text) - freq) ** 2
                  for letter, freq in english_freq.items())
  return fitness < fitness_threshold

