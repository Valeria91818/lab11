with open("txt.txt", 'r') as f:
    stroki = f.readline() 
numbers = stroki.split()
flag = 0
def num_to_words(digits):
    digit_words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(digit_words.get(digit, "неизвестно") for digit in digits)
for num in numbers:
    if num.isdigit() and len(num) >= 2:
        if int(num) % 2 == 0:
            if num[1] == '5' and num[-2] == '5':
                count_fives = num.count('5')
                if count_fives > 3:
                    flag += 1
                    print(num_to_words(num))