import re

ALPHABET: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

SPECIAL_CHARS: list = []

def count_words(text: str) -> int:
    word_count = text.split()
    return len(word_count)

def count_letters(text: str) -> dict[str, int]:
    letter_count: dict[str, int] = {}

    # populate dict with alphabet
    for letter in ALPHABET:
        letter_count[letter] = 0

    # count character 1 by 1
    for char in text:
        # ignore non-letters
        if re.findall("[A-Za-z]",char) == []:
            continue
        char = re.findall("[A-Za-z]",char)[0]
        # char = re.sub("[\"\',\s\(\)\.]-","",char)
        # if len(char) == 0:
        #     continue
        char = char.lower()
        letter_count[char] += 1
    return letter_count

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"The book has {word_count} words!")
        letter_count: dict = count_letters(file_contents)
        print(letter_count)


if __name__ == '__main__':
    main()