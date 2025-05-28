import re
with open("txt.txt",'r', encoding='utf-8') as f:
    stroki=f.readline()
numbers=stroki.split(',')  
flag=0
def num_to_words(digits):
    digit_words = {'0': '����','1': '����','2': '���','3': '���', '4': '������','5': '����','6': '�����','7': '����',}
    return digit_words.get(digits, "����������") 
for num in numbers:
    if re.fullmatch(r'\d{2,}', num):
        if int(num) % 2 == 0:
            if re.search(r'^.(5).*5.$', num): 
                if num.count('5') > 3: 
                    flag += 1
                    print(num_to_words(num))