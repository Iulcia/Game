num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:

    for i in range(num + 1):
        sum += i
        
    num = int(input("Enter integer (0 for output): "))

print(sum)

""""
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
        
    for i in range(num + 1):
        sum = sum + i
print(sum)
"""
        