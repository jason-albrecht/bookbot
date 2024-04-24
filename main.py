
def count_words(text: str):
    word_count = text.split()
    return len(word_count)

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)
        word_count = count_words(file_contents)
        print(f"The book has {word_count} words!")

if __name__ == '__main__':
    main()