import sys
from stats import get_book_report

def main():
    cli_arguments = sys.argv
    
    if len(cli_arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    get_book_report(cli_arguments[1])

main()
