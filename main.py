import random

def generate_random_list(min_value, max_value, count):
    return [random.randint(min_value, max_value) for _ in range(count)]

def main():
    try:
        min_val = int(input("Минимум: "))
        max_val = int(input("Максимум: "))
        count = int(input("Количество чисел: "))
    except ValueError:
        print("Ошибка ввода")
        return

    numbers = generate_random_list(min_val, max_val, count)

    print("\nРезультат:")
    print(numbers)

if __name__ == "__main__":
    main()