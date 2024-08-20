import threading

# Задание 1
user_list = [1, 2, 3, 4, 5, 6, 7, 132, 123, 12, 23, 35, -5, 0]

def find_max(user_list):
    print(f"Max: {max(user_list)}")

def find_min(user_list):
    print(f"Min: {min(user_list)}")

thread1 = threading.Thread(target=find_max, args=(user_list,))
thread2 = threading.Thread(target=find_min, args=(user_list,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Задание 2
def calculate_sum(user_list):
    print(f"Sum: {sum(user_list)}")

def calculate_average(user_list):
    average = sum(user_list) / len(user_list)
    print(f"Average: {average}")

user_list = [1, 2, 3, 4, 5, 6, 7, 132, 123, 12, 23, 35, -5, 0]

thread1 = threading.Thread(target=calculate_sum, args=(user_list,))
thread2 = threading.Thread(target=calculate_average, args=(user_list,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print()
# Задание 3
def write_even_numbers(numbers):
    even_numbers = [number for number in numbers if number.strip().isdigit() and int(number.strip()) % 2 == 0]
    with open("even_numbers.txt", "w") as file:
        for number in even_numbers:
            file.write(number.strip() + "\n")
    print(f"Even numbers: {len(even_numbers)}\n")

def write_odd_numbers(numbers):
    odd_numbers = [number for number in numbers if number.strip().isdigit() and int(number.strip()) % 2 != 0]
    with open("odd_numbers.txt", "w") as file:
        for number in odd_numbers:
            file.write(number.strip() + "\n")
    print(f"Odd numbers: {len(odd_numbers)}\n")

# user_input_filename = input("Enter the file name: ")
user_input_filename = "numbers.txt"
with open(user_input_filename, "r", encoding='utf-8') as file:
    numbers = file.read().split(',')

thread1 = threading.Thread(target=write_even_numbers, args=(numbers,))
thread2 = threading.Thread(target=write_odd_numbers, args=(numbers,))
thread1.start()
thread2.start()

thread1.join()
thread2.join()