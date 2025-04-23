from stats import get_book_character_count, get_book_report, get_book_text, get_book_word_count

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    character_dict = get_book_character_count(frankenstein)

    #print(f"{get_book_word_count(frankenstein)} words found in the document")
    #print()
    print(get_book_report(character_dict))

main()
