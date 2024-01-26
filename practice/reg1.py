for i in range(16):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    #print(s)


#width = 5
#for num in range(12):
 #   print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))    

s = "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
  
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    final_list = []
    k = 0
    for n, g in students.items():
         k += 1
         final_list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(k, n , g , grades.get(g)))

    return final_list

formatted_grades(students)    

#################################

print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111


def formatted_numbers():
    list = []

    list.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex","binary"))

    for i in range(16):
        dec = format(i, 'd')
        hex = format(i, 'x')
        bin = format(i, 'b')
        list.append("|{:<10}|{:^10}|{:>10}|".format(dec, hex ,bin))                     

    return list

print(formatted_numbers())