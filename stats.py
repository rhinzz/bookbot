def get_book_text(filepath: str):
  with open(filepath) as book:
    book_content = book.read()
    return book_content

def get_num_words(filepath: str):
  book_text = get_book_text(filepath)
  word_count = len(book_text.split())
  return f"Found {word_count} total words"

def get_char_count_dictionary(filepath: str):
  book_text = get_book_text(filepath)
  word_list = book_text.split()
  unique_char = {}
  for word in word_list:
    for char in word:
      if char.lower() not in unique_char:
        unique_char[char.lower()] = 0
      unique_char[char.lower()] += 1 
  return unique_char

def to_sorted(items):
  return items["num"]  

def get_char_count_list(filepath: str):
  char_count_list = []
  char_count_dictionary = get_char_count_dictionary(filepath)
  for entry in char_count_dictionary:
    if not entry.isalpha():
      continue
    char_count_list.append({"char": entry, "num": char_count_dictionary[entry]})
  char_count_list.sort(reverse=True, key=to_sorted)
  return char_count_list

