def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)

    ls = []
    for i in num_char:
        ls.append({i : num_char[i]})

    ls.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    
    for key in num_char:
        print(f"The '{key}' character was found {num_char[key]} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_char(text):
    char_dict = {}
    lowered_text = text.lower()
    for ch in lowered_text:
        if ch.isalpha():
            if ch in char_dict:
                char_dict[ch] += 1
            else:
                char_dict[ch] = 1
    return char_dict


def sort_on(dict):
    for char in dict:
        return dict[char]


main()