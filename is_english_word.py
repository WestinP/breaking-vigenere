def is_logically_english(text: str, percent: float) -> bool:
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

    count = 0
    for word in maybe_words:
        if word in real_words:
            count += 1
    if count / len(maybe_words) >= percent:
        return True
    return False


print(is_logically_english('hello adsasdasdwdasd', 0.90))
