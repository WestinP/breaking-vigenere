
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
    max_period = 10  # Maximum key length to consider
    best_period = 1
    best_ic = 0
    for period in range(1, max_period + 1):
        slices = [''] * period
        for i in range(len(text)):
            slices[i % period] += text[i]  # Split the text into slices
        sum = 0
        for i in range(period):
            sum += ioc(slices[i])  # Sum the index of coincidences of each slice
        index_of_coincidence_average = sum / period
        if index_of_coincidence_average > best_ic:  # If the average index of coincidence is greater than the best so far
            best_ic = index_of_coincidence_average
            best_period = period
    return best_period  # Return the key length that gives the highest average index of coincidence
