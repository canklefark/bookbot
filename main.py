import sys

from stats import num_letters, num_words, sort_dictionary


def get_book_text(filepath):
  with open(filepath) as f:
    book_contents = f.read()
  return book_contents

def main(filepath):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words(get_book_text(filepath))} total words")
  print("--------- Character Count -------")
  dicts = sort_dictionary(num_letters(get_book_text(filepath)))
  for item in dicts:
    if item["char"].isalpha():
      print(f"{item['char']}: {item['num']}")
  print("============= END ===============")

if len(sys.argv) == 2:
  main(sys.argv[1])
else:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
