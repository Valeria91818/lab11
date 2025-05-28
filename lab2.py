import re
with open("txt.txt",'r', encoding='utf-8') as f:
    stroki=f.readline()
numbers=stroki.split(',')  
flag=0
def num_to_words(digits):
    digit_words = {'0': 'íîëü','1': 'îäèí','2': 'äâà','3': 'òðè', '4': '÷åòûðå','5': 'ïÿòü','6': 'øåñòü','7': 'ñåìü',}
    return digit_words.get(digits, "íåèçâåñòíî") 
for num in numbers:
    if re.fullmatch(r'\d{2,}', num):
        if int(num) % 2 == 0:
            if re.search(r'^.(5).*5.$', num): 
                if num.count('5') > 3: 
                    flag += 1
                    print(num_to_words(num))
