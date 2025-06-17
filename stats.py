def get_num_words(book):
  words = book.split()
  word_count = len(words)
  return word_count

def num_of_chars(book):
  characters = {}
  for word in book:
    for char in word.lower():
      if char in characters:
        characters[char] += 1
      else:
        characters[char] = 1
  return characters

def sort_characters(characters):
  sorted_characters = []
  for char in characters:
    sorted_characters.append({"char": char, "num": characters[char]})
  sorted_characters.sort(reverse=True, key=sort_on)
  return sorted_characters

def sort_on(dict):
  return dict["num"]