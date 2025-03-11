def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_words_length(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    char_count = {}
    for char in book_text.lower():
        if char.isalpha():
            if( char in char_count):
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_char(char_count):
    return sorted(char_count.items(), key=lambda item: item[1], reverse=True)

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    return get_book_words_length(book_text)

def get_num_characters(filepath):
    book_text = get_book_text(filepath)
    char_count = get_char_count(book_text)
    return sort_char(char_count)