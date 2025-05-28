# ����������� �� ����� ���������
def generate_numbers_with_limit(length, n, max_sum):
    result = []
    current_sum = 0
    while len(result) < length:
        num = random.randint(0, n - 1)
        if current_sum + num <= max_sum:
            result.append(num)
            current_sum += num
    return result

# ������� �������
def unique_count(array):
    return len(set(array))

# ��������� ������� ����������
max_sum = 10
algorithmic_time_with_limit = timeit.timeit(lambda: generate_numbers_with_limit(length, n, max_sum), number=10000)
unique_count_result = unique_count(algorithmic_result)

print(f"��������������� ������ � ������������: {algorithmic_time_with_limit:.6f} ������")
print(f"���������� ���������� ��������: {unique_count_result}")

# ��������� ������ ������� � ������ �����������
limited_result = generate_numbers_with_limit(length, n, max_sum)
limited_unique_count = unique_count(limited_result)

print("��������� � ������������:", limited_result)
print("���������� ���������� �������� � ������������:", limited_unique_count)