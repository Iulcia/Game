def format_string(string, length):
    if len(string) >= length:
        result = string
    else:
        result = " " * ((length - len(string)) // 2) + string
        
    return f'{result}'

def first(size, *topics):
    return len(size) + len(topics)

def second(size, **keys):

    return len(keys)

''''Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.
Тести на правильність роботи функції виконуються для наступних наборів аргументів:

string='aaaaaaaaaaaaaaaaac', length=12
length=15, string='abaa'''    

def cost_delivery(quantity, *agrs, discount = 0):

    if quantity == 1:
        result = 5 * (1 - discount)
    else:
        result = (5 + 2 * (quantity - 1)) * (1 - discount)

    return result

print(cost_delivery(2, 1, 2, 3, discount=0.5))