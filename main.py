import sys
from stats import get_num_words
from stats import num_of_chars
from stats import sort_characters

def get_book_test(filepath):
  file_contents = ""
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main(path):
  book = get_book_test(path)
  num_words = get_num_words(book)
  characters = num_of_chars(book)
  sorted_characters = sort_characters(characters)
  report = create_report(path, num_words, sorted_characters)
  print(report)

def create_report(path, num_words, sorted_characters):
  report = "============ BOOKBOT ============"
  report += f"\nAnalyzing book found at {path}..."
  report += "\n----------- Word Count ----------"
  report += f"\nFound {num_words} total words"
  report += "\n--------- Character Count -------"

  for char in sorted_characters:
    if char["char"].isalpha():
      report += f"\n{char["char"]}: {str(char["num"])}"
  report += "\n============= END ==============="
  return report

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

main(sys.argv[1])