import re

def find_all_words(text, word):

    list = []

    list = re.findall(word, text, flags = re.IGNORECASE)

    return list


text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn"
word = "Python"

print(find_all_words(text, word))

#####################################

p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
print(p)  # color socks and color shoes

def replace_spam_words(text, spam_words):

    for spam in spam_words:
        text = re.sub(spam, len(spam) * "*", text, flags=re.IGNORECASE)
    return text


def find_all_emails(text):
    result = re.findall(r"[A-Za-z][\w.%+-]{1,}@[A-Za-z]+\.[A-Za-z]{2,}", text)
    return result

import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"(?:http|https)://[a-zA-Z]+\.[a-zA-Z]+(\.[a-zA-Z]+)?", text)
    for match in iterator:
        result.append(match.group())
    return result


def my_func(a, b):
    return a / b

result = my_func(5, 2)
print(result)