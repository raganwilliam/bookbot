def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

def get_word_count(contents_of_book):
    num_words = 0
    for words in contents_of_book.split():
        num_words += 1
    return num_words

def get_char_count(contents_of_book):
    char_dict = {}
    for char_key in contents_of_book.lower():
        
        if char_key in char_dict:
            char_dict[char_key] += 1
        else:
            char_dict[char_key] = 1

    return char_dict


def sort_char(char_dict):
    char_list = []

    for char_key, count_key in char_dict.items():
            if char_key.isalpha():
                alpha_dict = {"char": char_key, "num": count_key}
                char_list.append(alpha_dict)
        
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list


