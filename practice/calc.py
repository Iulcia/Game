wait_for_number = True
operator = None
operand = None
result = None
while True:
    user_input = input(">>>")

    if user_input == "=":
        print(result)
        break

    if wait_for_number:    
        try:
            operand = int(user_input)
            wait_for_number = False
        except ValueError as e:
            print(f"Not a number. {e}")
    else:
        if user_input in "+-*/":
            operator = user_input
            wait_for_number = True
        else:
            print(f" {user_input} is not '+' or '-' or '/' or '*'. Try again")
            continue

    if not result:
        result = operand
        operand = None
        continue

    if operand and operator:
        if operator == "+":
            result += operand
        if operator == "-":
            result -= operand 
        if operator == "*":
            result *= operand
        if operator == "/":
            result /= operand       

        operator = None
        operand = None