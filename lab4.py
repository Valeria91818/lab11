import numpy as np
import matplotlib.pyplot as plt
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def reader(filename):  
    with open(filename, 'r') as file:
        return [list(map(int, line.split())) for line in file]
k = int(input("Введите k: "))
n = int(input("Введите n: "))
A = np.array(reader('matrix2.txt'))[:n, :n]  
print("Исходная матрица A:\n", A)
F = np.copy(A)
half = n // 2
if n % 2 == 0:
    B = F[:half, half:]
    C = F[half:, :half]
    E = F[half:, half:]
else:
    B = F[:half, half+1:]
    C = F[half+1:, :half]
    E = F[half+1:, half+1:]
prime_count = 0
for j in range(1, B.shape[1], 2):
    for i in range(B.shape[0]):
        if is_prime(B[i, j]):
            prime_count += 1
sum_even_rows = 0
for i in range(1, B.shape[0], 2): 
    sum_even_rows += np.sum(B[i, :])
print(f"\nКоличество простых в нечетных столбцах B: {prime_count}")
print(f"Сумма чисел в четных строках B: {sum_even_rows}")
if prime_count > sum_even_rows:
    print("\nМеняем B и E симметрично")
    if n % 2 == 0:
        F[:half, half:], F[half:, half:] = np.flipud(E), np.flipud(B)
    else:
        F[:half, half+1:], F[half+1:, half+1:] = np.flipud(E), np.flipud(B)
else:
    print("\nМеняем C и E несимметрично")
    if n % 2 == 0:
        F[half:, :half], F[half:, half:] = E.copy(), C.copy()
    else:
        F[half+1:, :half], F[half+1:, half+1:] = E.copy(), C.copy()
print("\nМатрица F после преобразований:\n", F)
try:
    A_inv = np.linalg.inv(A)
    F_inv = np.linalg.inv(F)
    G = np.tril(A) 
except np.linalg.LinAlgError:
    print("Ошибка: одна из матриц вырождена, невозможно вычислить обратную матрицу")
    exit()
diag_sum_F = np.trace(F)
det_A = np.linalg.det(A)
print(f"\nОпределитель A: {det_A}")
print(f"Сумма диагональных элементов F: {diag_sum_F}")
if det_A > diag_sum_F:
    print("\nВычисляем выражение: A⁻¹*Aᵀ - K*F⁻¹")
    term1 = np.dot(A_inv, A.T)
    term2 = k * F_inv
    VIR = term1 - term2
    print("\nA⁻¹:\n", A_inv)
    print("\nAᵀ:\n", A.T)
    print("\nA⁻¹*Aᵀ:\n", term1)
    print("\nF⁻¹:\n", F_inv)
    print("\nK*F⁻¹:\n", term2)
else:
    print("\nВычисляем выражение: (A⁻¹ + G - F⁻¹)*K")
    term1 = A_inv + G - F_inv
    VIR = term1 * k
    
    print("\nA⁻¹:\n", A_inv)
    print("\nG:\n", G)
    print("\nF⁻¹:\n", F_inv)
    print("\nA⁻¹ + G - F⁻¹:\n", term1)
print("\nРезультат вычислений (VIR):\n", VIR)
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.imshow(F, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Тепловая карта F")
plt.subplot(132)
plt.plot(F.sum(axis=1), 'o-', color='green')
plt.title("Сумма по строкам")
plt.grid(True)
plt.subplot(133)
plt.bar(range(F.shape[1]), F.sum(axis=0), color='green', alpha=0.6)
plt.title("Сумма по столбцам")
plt.grid(True)
plt.tight_layout()
plt.show()
