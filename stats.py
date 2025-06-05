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


def sort_chars(dict_chars):
    sort_list = []
    for char in dict_chars:
        new_dict = {"char": char, "num": dict_chars[char]}
        sort_list.append(new_dict)
    sort_list.sort(key=lambda dict: dict["num"], reverse=True)
    return sort_list
