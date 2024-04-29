
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def ioc(text: str):
    frequency = [0]*26 # frequency of each letter in the alphabet
    total = 0
    for char in text:
        if char in ALPHABET:
            frequency[ALPHABET.index(char)] += 1 # increment the frequency of the letter
            total += 1
    ic = 0
    numerator = 0
    for i in range(26):
        numerator += frequency[i] * (frequency[i] - 1)  # Sum the numerators
    if total > 1:  # Avoid division by zero
        ic = 26 * numerator / (total * (total - 1))
    return ic

def ioc_period(text: str):
    found = False
    period = 0
    while not found:
        period += 1
        slices = [''] * period
        for i in range(len(text)):
            slices[i % period] += text[i] # Split the text into slices
        sum = 0
        for i in range(period):
            sum += ioc(slices[i]) # Sum the index of coincidences of each slice
        index_of_coincidence_average = sum / period
        if index_of_coincidence_average > 1.6: # If the average index of coincidence is greater than 1.6, the period is found
            found = True
            return period
