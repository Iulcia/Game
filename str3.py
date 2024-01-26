def is_spam_words(text, spam_words, space_around=False):

    if space_around == True:
         for word in spam_words:
             return True if word.lower() in text.lower().replace(".","").split(" ") else False
    else:    
        for word in spam_words:
            if word.lower() in text.lower():
                return True
                break
            else:
                ...

print(is_spam_words("Молох", ["лох"]))

#TRANSLATE

CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LATIN = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANSLIT_DICT = {}

def translate(name):

    for c, l in zip(CYRILLIC, LATIN):
        TRANSLIT_DICT[ord(c)] = l
        TRANSLIT_DICT[ord(c.upper())] = l.upper()

    return name.translate(TRANSLIT_DICT)

#print("Дмитро Короб".translate(TRANSLIT_DICT))  # chasha
#print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA

print(translate ("Дмитро Короб"))
print(translate("Олекса Івасюк"))