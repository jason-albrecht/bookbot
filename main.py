import re

ALPHABET: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# SPECIAL_CHARS: list = []

def count_words(text: str) -> int:
    word_count = text.split()
    return len(word_count)

def count_letters(text: str) -> dict[str, int]:
    letter_count: dict[str, int] = {}

    # set up letters for counting
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

def get_dict_value(dictionary):
    return dictionary[1]

def sort_on(dictionary: dict[str,int]) -> list:
    sorted_dict = sorted(dictionary.items(), key=get_dict_value, reverse=True)
    return sorted_dict
    # items: list = []

    # for idx, key in enumerate(dictionary):
    #     item: dict = {}
    #     item[key] = dictionary[key]

        # items.append(item)
    # return items

def print_rank(dictionary: dict):
    pass
    

def main():
    path: str = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"--- Begin report of {path} ---")
        print(f"{word_count} words found in the document!")
        print(" ")
        letter_count: list = count_letters(file_contents)
        # print(letter_count)
        letter_rank = sort_on(letter_count)
        for letter, count in letter_rank:
            print(f"The '{letter}' character was found {count} times")
        # letter_rank.sort(reverse=True, key=sort_on)
        print("--- End report ---")
            



if __name__ == '__main__':
    main()