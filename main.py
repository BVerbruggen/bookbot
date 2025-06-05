from stats import count_words, count_chars, sort_chars
import sys


def get_book_text(filepath):
    with open(filepath, encoding='utf-8-sig') as f:
        return f.read()


def main(book_path):
    print("================ BOOKBOT ==================")
    print(f"Analyzing book found at {book_path}")

    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print("---------------- Word Count --------------")
    print(f"Found {num_words} total words")
    num_chars = sort_chars(count_chars(book_text))
    print("------------- Character Count ------------")
    for d in num_chars:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
