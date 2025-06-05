from stats import count_words, count_chars


def get_book_text(filepath):
    with open(filepath, encoding='utf-8-sig') as f:
        return f.read()


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    num_chars = count_chars(book_text)
    print(num_chars)


main()
