s = 'Some words'

#print(s.rfind('o')) # 6

s = "I am learning strings in Python. Some new methods got now."
sentences = s.split(". ")

#print(sentences[0]) # I am learning strings in Python
#print(sentences[1]) # Some new methods got now.

#sentences = ["I am learning strings in Python", "Some new methods got now."]
text = ". ".join(sentences)
#print(text) # I am learning strings in Python. Some new methods got now.

dogs_text = "All dogs bark like dogs."
cats_text = dogs_text.replace("dogs", "cats")
#print(cats_text) # All cats bark like cats.


def real_len(text):
    len = 0
    for i in text:
        if 9 <= ord(i) <= 13:
            pass
        else:
            len += 1
    return len

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    }
]


def find_articles(search, letter_case = False):

    words = []
    result = 0
    pos = []
    final = []

    for key in articles_dict:
        for v in key:
            if v == "author" or v == "title":
                words.append((key.get(v).split(" ")))
    for k in words:
        for el in k:
            if letter_case == True:
                if search in el:
                    result += 1
                    pos.append(words.index((k)) //2 )

                else:
                    ...    
            else:
                if search.lower() in el.lower():
                    result += 1
                    pos.append(words.index((k)) //2 )

                else:
                    ... 

    if len(pos) != 0:
        for i in articles_dict:
            if articles_dict.index(i) in pos:
                final.append(i)
            else:
                ...

    return(final)

 

print(find_articles("Ocean"))