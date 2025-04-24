def get_book_unsorted_character_count_dict(book_contents):
    characters = {}

    for char in book_contents.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def get_book_sorted_character_count(unsorted_character_count_dict):
    # Iterate through unsorted dict:
        # If the character is alphabetical:
            # If sorted dict is empty
                # add the first unsorted dict to it
            # else:
                # Iterate over the sorted dict and compare the current unsorted dict to the counts of the sorted dict
                    # If current unsorted dict's count is < current sorted dict's count:
                        # insert before
                    # elif at the end of the sorted dict:
                        # append

    sorted_character_dicts_list = []

    for unsorted_char in unsorted_character_count_dict:
        unsorted_count = unsorted_character_count_dict[unsorted_char]

        if unsorted_char.isalpha():
            if len(sorted_character_dicts_list) == 0:
                # print(f"Appending {unsorted_char} and {unsorted_count} to the sorted dict because it's empty")
                sorted_character_dicts_list.append({ unsorted_char: unsorted_count })
            else:
                # "Linear sort"
                for sorted_index in range(0, len(sorted_character_dicts_list)):
                    char_dict = sorted_character_dicts_list[sorted_index]
                    char_dict_count = list(char_dict.values())[0]

                    # print(f"Character dictionary: {char_dict} at for index of {sorted_index}")
                    # print(f"Unsorted char: {unsorted_char}; count: {unsorted_count}")
                    # print(len(sorted_character_dicts_list))

                    # If char_dict count is less than the current index, insert before
                    if unsorted_count < char_dict_count:
                        # print(f"Inserting {unsorted_char} and {unsorted_count} at index {sorted_index}")
                        sorted_character_dicts_list.insert(sorted_index, { unsorted_char: unsorted_count })
                        break

                    # else append
                    elif sorted_index == len(sorted_character_dicts_list) - 1:
                        # print(f"Appending {unsorted_char} and {unsorted_count}")
                        sorted_character_dicts_list.append({ unsorted_char: unsorted_count })
                        break

    return sorted_character_dicts_list

def get_book_report(filepath):
    unsorted_character_count_dict = get_book_unsorted_character_count_dict(get_book_text(filepath))
    sorted_character_dicts_list = get_book_sorted_character_count(unsorted_character_count_dict)
    word_count = get_book_word_count(get_book_text(filepath))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in reversed(sorted_character_dicts_list):
        key, value = next(iter(char_dict.items()))
        print(f"{key}: {value}")

    print("============= END ===============")

def get_book_text(filepath):
    file_contents = ""
    path = "./" + filepath

    with open(path) as f:
        file_contents = f.read()

    return file_contents

def get_book_word_count(book_contents):
    words = book_contents.split()

    return len(words)

