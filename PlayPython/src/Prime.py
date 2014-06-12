# coding=Big5

number = int(input('輸入數字：'))
half = number // 2
for num in range(2, half + 1):
    if (number % num) == 0:
        print(number, 'No')
        break
else:
    print(number, 'Yes')