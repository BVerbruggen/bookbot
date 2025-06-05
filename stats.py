def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    dict_chars = {}

    for char in text:
        if char.lower() in dict_chars:
            dict_chars[char.lower()] += 1
        else:
            dict_chars[char.lower()] = 1

    return dict_chars
