num = int(input("Input number "))
fizz = 5
buzz = 3

if num % fizz*buzz == 0:
    message = f' {num} has fizzbuzz'
elif num % fizz == 0:
    message = f' {num} has fizz'    
elif num % buzz == 0:
    message = f' {num} has buzz'  
else:
     message = f' {num}'       

print(message)

def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

print(string_to_codes('Yuliia'))

def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
        
    apply_discount()   
    return price

print(discount_price(50, 0.5))

def get_fullname(first_name, last_name, middle_name = ""):
    if middle_name != "":
        return f'{first_name} {middle_name} {last_name}'
    else:
        return f'{first_name} {last_name}'
    
print(get_fullname('Yuliia', 'Rodionova', 'Sergiivna'))  

def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        k = (length - len(string)) // 2
        space = " "*k
        if not (length - len(string)) % 2:
            return f'{space}{string}{space}|'
        else:
            bspace = " "*(k+1)
            return f'{space}{string}{bspace}|' 
    
print(format_string("abba",1)) 

def first(size, *params):
    return size + len(params)
    
def second(size, **params):
    return size + len(params) 

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):

    return int(factorial(n)/(factorial(n-k)*factorial(k)))