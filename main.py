from stats import get_num_words, get_num_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    dir_book = sys.argv[1]
    num_words = get_num_words(dir_book)
    characte_num = get_num_characters(dir_book)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {dir_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in characte_num:
        print(f"{char}: {count}")


main()