def sort_on(items):
  return items["num"]

def num_words(book_text):
  word_counter = 0
  split_text = book_text.split()

  for words in split_text:
    word_counter += 1

  return(word_counter)

def num_letters(book_text):
  formatted_text = book_text.lower()
  split_text = formatted_text.split()
  letter_counter = {}
  # print(split_text)

  for word in split_text:
    for char in word:
      if char.isalpha():
        if char in letter_counter:
          letter_counter[char] += 1
        else:
          letter_counter[char] = 1
  return letter_counter

def sort_dictionary(dict):
  sorted_list = []
  dict_items = dict.items()
  for char, num in dict_items:
    sorted_dict = {"char": char, "num": num}
    sorted_list.append(sorted_dict)

  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list
