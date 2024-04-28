def is_logically_english(text: str, percent: float) -> float:
    maybe_words = text.split()
    if len(maybe_words) == 0:
        return False
    real_words = {}
    filereader = open('dictionary.txt', 'r')
    dictionary = filereader.readlines()
    filereader.close()
    for word in dictionary:
        word = word.strip()
        word = word.lower()
        real_words[word] = 1
    print('Real Words:', real_words)
