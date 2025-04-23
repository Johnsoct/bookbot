def get_book_character_count(book_contents):
    characters = {}

    for char in book_contents.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def get_book_report(unsorted_character_count_dict):
    report = ""
    sorted_character_count_dict = []

    for char in unsorted_character_count_dict:
        count = unsorted_character_count_dict[char]

        if char.isalpha():
            if len(sorted_character_count_dict) == 0:
                sorted_character_count_dict.append({ char: count })
            else:
                # Linear "sort"
                for index in range(0, len(sorted_character_count_dict) + 1):
                    char_dict = sorted_character_count_dict[index]

                    print(char_dict)
                    # if less than 0, insert at 0
                    if count < list(char_dict.values())[0]:
                        sorted_character_count_dict[index:index] = { char: count }
                    # if greater than 0, check against 1, repeat
                    else:
                        sorted_character_count_dict.append({ char: count })

    print(sorted_character_count_dict)

    return report

def get_book_text(filepath):
    file_contents = ""
    
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_book_word_count(book_contents):
    words = book_contents.split()

    return len(words)

