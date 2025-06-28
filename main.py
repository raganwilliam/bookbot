from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    contents_of_book = get_book_text(file_path)
    char_dict = get_char_count(contents_of_book)
    char_list = sort_char(char_dict)

 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(contents_of_book)} total words")
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
        

main()
    



