def get_num_words(input_string):
  list = input_string.split()
  return len(list)

def get_num_chars(input_string):
  all_char_dic = {};
  for char in input_string:
    normalized_char = char.lower()
    if normalized_char in all_char_dic:
      all_char_dic[normalized_char] += 1
    else:
      all_char_dic[normalized_char] = 1
  return all_char_dic

def sort_on(item):
    return next(iter(item.values()))
    #return item[key]
 
def sort_dict(in_dictionary):
  # convert to list
  result = []
  for i in in_dictionary:
    result.append( {i: in_dictionary[i]})
  result.sort(reverse=True, key=sort_on)
  return result