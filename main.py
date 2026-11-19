from calculator_pkg.input_data import get_user_input
from calculator_pkg.operations import calculate
from calculator_pkg.output_data import print_result


def main():
    try:
        num1, op, num2 = get_user_input()
        result = calculate(num1, op, num2)
        print_result(num1, op, num2, result)
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
