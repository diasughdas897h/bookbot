import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict 

def get_book_txt(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def print_list_with_dict(list):
  for el in list:
    key = next(iter(el.keys()))
    if key.isalpha():
      key = next(iter(el.keys()))
      print(f"{key}: {el[key]}")

def main():
  #filepath = "books/frankenstein.txt"
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  filepath = sys.argv[1]
  book = get_book_txt(filepath)
  num_words = get_num_words(book)
  char_map = (get_num_chars(book))
  sorted_list = sort_dict(char_map)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  print_list_with_dict(sorted_list)


main()
