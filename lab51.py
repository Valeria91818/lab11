import timeit
import random
length = 10  
n = 4        
# Алгоритмический подход
def generate_numbers_algorithmic(length, n):
    result = []
    for _ in range(length):
        result.append(random.randint(0, n - 1))
    return result
# Функциональный подход
def generate_numbers_functional(length, n):
    return [random.randint(0, n - 1) for _ in range(length)]
# Сравнение времени выполнения
algorithmic_time = timeit.timeit(lambda: generate_numbers_algorithmic(length, n), number=10000)
functional_time = timeit.timeit(lambda: generate_numbers_functional(length, n), number=10000)
print(f"Алгоритмический подход: {algorithmic_time:.6f} секунд")
print(f"Функциональный подход: {functional_time:.6f} секунд")
# Генерация размещений
algorithmic_result = generate_numbers_algorithmic(length, n)
functional_result = generate_numbers_functional(length, n)
print("Алгоритмический результат:", algorithmic_result)
print("Функциональный результат:", functional_result)
