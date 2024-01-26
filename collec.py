
def amount_payment(payment):

    sum = 0
    for value in payment:
        if value > 0:
            sum += value
        
    return sum    
    
def prepare_data(data):

    data.remove(min(data))
    data.remove(max(data))
    data.sort()

    return data

def format_ingredients(data):
    my_string = ''

    if len(data) == 0:
        my_string = my_string
    elif len(data) == 1:
        my_string += data[0]
    else:    
        for i in data:
            if i in data[: len(data)-2]:
                my_string += i + "," + " "
            elif i in data[-2]:
                my_string += i + " and" + " "
            else:
                my_string += i 

    return my_string


'''1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly'''
    
def get_grade(key):

    dict = {'A': 5, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 'FX': 2, 'F': 1}

    return dict.get(key)

def get_description(key):

     dict = {'A': 'Perfectly', 'B': 'Very good', 'C': 'Good', 'D': 'Satisfactorily', 'E': 'Enough', 'FX': 'Unsatisfactorily', 'F': 'Unsatisfactorily'}

     return dict.get(key)

def lookup_key(data, search):
    new_list = []

    for i, value in data.items():       
        if value == search:
            new_list.append(i)

    return new_list

dict = {'A': 5, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 'FX': 2, 'F': 1}

def split_list(grade):
    
    less = []
    bigger = []  

    if len(grade) > 0:

        sum = 0
        average = 0
        for i in grade:
            sum += i

        average = sum / len(grade)   

        for i in grade:
            if i <= average:
                less.append(i)
            else:
                bigger.append(i)    

    return less, bigger

grad =[]

print(split_list(grad))

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

coordinates = [0, 1, 3, 2, 0, 2]

def calc_distance(coords):
    if len(coords) <= 1:
        return 0
    
    total_distance = 0
    
    # print(len(coords) - 1)
    for index in range(len(coords) - 1):
        # print(index, dot)
        dot1 = coords[index]
        dot2 = coords[index + 1]
        # key = [dot1, dot2]
        # key.sort()
        # if dot1 > dot2:
        #     dot1, dot2 = dot2, dot1
        total_distance += points[tuple(sorted([dot1, dot2]))]
    return total_distance
    
distance = calc_distance(coordinates)
print(distance)