import re

s = "I am 25 years old"
age = re.search('\d+', s)
#print(age)  # <re.Match object; span=(5, 7), match='25'>
#print(age.group())

################################################

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "python"

import re


def find_word(text, word):
    dict = {'result': False, 'first_index': None,'last_index': None, 'search_string': word,'string': text }

    found = re.search(word, text)   

    if found:
        from_to = found.span()
        dict['result'] = True
        dict['first_index'] = from_to[0]
        dict['last_index'] = from_to[1] 

    return dict

print(find_word(text, word))

