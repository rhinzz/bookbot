import sys
import os.path
from stats import get_num_words, get_char_count_list

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  if os.path.exists(sys.argv[1]) is not True:
    print(f"Error: File {sys.argv[1]} not found")
    sys.exit(1)
  if sys.argv[1].endswith(".txt") is not True:
    print(f"Error: File {sys.argv[1]} does not ends with '.txt'")
    sys.exit(1)
    
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(get_num_words(sys.argv[1]))
  print("--------- Character Count -------")
  char_count_list = get_char_count_list(sys.argv[1])
  for entry in char_count_list:
    print(f"{entry["char"]}: {entry["num"]}")
  print("============= END ===============")

main()