message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if ord('a') <= ord(ch) <= ord('z'):
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        new_char = chr(pos + ord('a'))
        encoded_message += new_char
    elif ord('A') <= ord(ch) <= ord('Z'):
        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26
        new_char = chr(pos + ord('A'))
        encoded_message += new_char   
    else:
        new_char = ch
        encoded_message += new_char                    

print(encoded_message)
