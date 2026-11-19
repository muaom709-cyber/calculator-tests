def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно")
        return num1 / num2
    else:
        raise ValueError("Неизвестная операция")
