from stats import word_count
from stats import char_count
from stats import sorted_char_count
import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()
   


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    result = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(result)} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count(result):
        print(f"{item['char']}: {item['num']}")


    
main()