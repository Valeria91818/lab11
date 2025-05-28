with open("txt.txt", 'r') as f:
    stroki = f.readline() 
numbers = stroki.split()
flag = 0
def num_to_words(digits):
    digit_words = {
        '0': 'íîëü', '1': 'îäèí', '2': 'äâà', '3': 'òðè', '4': '÷åòûðå', '5': 'ïÿòü', '6': 'øåñòü', '7': 'ñåìü', '8': 'âîñåìü', '9': 'äåâÿòü'
    }
    return ' '.join(digit_words.get(digit, "íåèçâåñòíî") for digit in digits)
for num in numbers:
    if num.isdigit() and len(num) >= 2:
        if int(num) % 2 == 0:
            if num[1] == '5' and num[-2] == '5':
                count_fives = num.count('5')
                if count_fives > 3:
                    flag += 1
                    print(num_to_words(num))
