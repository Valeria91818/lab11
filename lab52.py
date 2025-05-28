import itertools
numbers = [0, 1, 2, 3]
def generate_arrays_recursive(K):
    """Рекурсивная генерация массивов с уникальными числами 0, 1, 2, 3"""
    arrays = []
    def backtrack(current_array):
        if len(current_array) == K:
            arrays.append(current_array.copy())
            return
        for num in numbers:
            if num not in current_array:  # Проверка на уникальность
                current_array.append(num)
                backtrack(current_array)
                current_array.pop()
    backtrack([])
    return arrays
def generate_arrays_itertools(K):
    """Генерация массивов через itertools.permutations"""
    if K > len(numbers):
        return [] 
    arrays = itertools.permutations(numbers, K)
    return [list(arr) for arr in arrays]
def find_optimal_array(arrays):
    """Находит массив с максимальной суммой"""
    if not arrays:
        return None, -1  
    max_sum = -1
    optimal_array = None
    for arr in arrays:
        current_sum = sum(arr)
        if current_sum > max_sum:
            max_sum = current_sum
            optimal_array = arr
    return optimal_array, max_sum
def main():
    try:
        K = int(input("Введите длину массива K: "))
    except ValueError:
        print("Ошибка: K должно быть целым числом!")
        return
    print("\n=== Рекурсивный метод ===")
    arrays_recursive = generate_arrays_recursive(K)
    if not arrays_recursive:
        print(f"Невозможно создать массив длины {K} из чисел 0, 1, 2, 3 (K должно быть ≤ 4)")
    else:
        optimal_recursive, sum_recursive = find_optimal_array(arrays_recursive)
        print(f"Всего массивов: {len(arrays_recursive)}")
        print(f"Оптимальный массив (сумма = {sum_recursive}): {optimal_recursive}")
    print("\n=== Метод с itertools ===")
    arrays_itertools = generate_arrays_itertools(K)
    if not arrays_itertools:
        print(f"Невозможно создать массив длины {K} из чисел 0, 1, 2, 3 (K должно быть ≤ 4)")
    else:
        optimal_itertools, sum_itertools = find_optimal_array(arrays_itertools)
        print(f"Всего массивов: {len(arrays_itertools)}")
        print(f"Оптимальный массив (сумма = {sum_itertools}): {optimal_itertools}")

