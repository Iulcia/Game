user_1 = {"name": "Jane", "age": 21}
user_2 = {"name": "Moris", "age": 23}
user_3 = {"name": "Steve", "age": 24}

persons = [user_1, user_2, user_3]

'''for user in persons:
    for field in user:
        print(user.get(field)) '''


def game(terra, power):

    for i in terra:
        for k in i:
            if k <= power:
                power += k
            else:
                break    
    return power


def is_valid_pin_codes(pin_codes):

    if len(pin_codes) == 0:
        
        return False
    
    set_pins = set(pin_codes)

    if len(pin_codes) == len(set_pins):
        try:
            for i in pin_codes:
                if isinstance(i,str) and len(i) == 4 and int(i):
                    pass
                else:
                    return False
            return True
        except ValueError:
            return False
    else:
        return False

from random import randint

def get_random_password():

    str = ''
    for i in range(8):
        random_symbol = chr(randint(40, 126))
        str += random_symbol

    return str

def is_valid_password(password):

    if len(password) == 8:
       for i in password:
           if i.isupper():
               for k in password:
                   if k.islower():
                       for m in password:
                           if 48<= ord(m) <=57:
                               return True
                           else:
                               pass
                       #return True
                   else:
                       pass
               #return True
           else:
               pass     

       return False
    else:
        return False        

passw = (get_random_password())

print( is_valid_password('aaaa8RBB'))



