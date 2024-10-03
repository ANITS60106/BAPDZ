def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        raise ValueError("Введите неотрицательное число.")
    return bin(decimal_number).replace("0b", "")

def binary_to_decimal(binary_string):
    if not all(bit in '01' for bit in binary_string):
        raise ValueError("Введите корректное двоичное число.")
    return int(binary_string, 2)

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Преобразовать десятичное число в двоичное")
        print("2. Преобразовать двоичное число в десятичное")
        print("3. Выход")

        choice = input("Введите номер действия (1/2/3): ")

        if choice == '1':
            try:
                decimal_number = int(input("Введите десятичное число: "))
                binary_number = decimal_to_binary(decimal_number)
                print(f"Десятичное число {decimal_number} в двоичной системе: {binary_number}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            binary_input = input("Введите двоичное число: ")
            try:
                decimal_output = binary_to_decimal(binary_input)
                print(f"Двоичное число {binary_input} в десятичной системе: {decimal_output}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод, попробуйте снова.")
