print('Шифрование или дешифрование?')
x = input()
x = x.lower()
if x == 'шифрование':
    print('Язык алфавита?')
    y = input()
    y = y.lower()
    if y == 'английский' or y == 'english':
        chars_low = 'abcdefghijklmnopqrstuvwxyz'
        chars_low = list(chars_low)
        chars_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars_up = list(chars_up)
        print('Каков шаг сдвига?')
        shag = int(input())
        print('Введите сообщение')
        s = input()
        s = list(s)
        for i in range(len(s)):
            if s[i] in chars_up:
                j = chars_up.index(s[i])
                if j+shag <= 25:
                    s[i] = chars_up[j+shag]
                else:
                    s[i] = chars_up[j+shag-26]
            if s[i] in chars_low:
                j = chars_low.index(s[i])
                if j+shag <= 25:
                    s[i] = chars_low[j+shag]
                else:
                    s[i] = chars_low[j+shag-26]
        shifr = ''.join(s)
        print(shifr)
    elif y == 'русский' or y == 'russian':
        chars_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        chars_low = list(chars_low)
        chars_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        chars_up = list(chars_up)
        print('Каков шаг сдвига?')
        shag = int(input())
        print('Введите сообщение')
        s = input()
        s = list(s)
        for i in range(len(s)):
            if s[i] in chars_up:
                j = chars_up.index(s[i])
                if j+shag <= 31:
                    s[i] = chars_up[j+shag]
                else:
                    s[i] = chars_up[j+shag-32]
            if s[i] in chars_low:
                j = chars_low.index(s[i])
                if j+shag <= 31:
                    s[i] = chars_low[j+shag]
                else:
                    s[i] = chars_low[j+shag-32]
        shifr = ''.join(s)
        print(shifr)
elif x == 'дешифрование':
    print('Язык алфавита?')
    y = input()
    y = y.lower()
    if y == 'английский' or y == 'english':
        chars_low = 'abcdefghijklmnopqrstuvwxyz'
        chars_low = list(chars_low)
        chars_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars_up = list(chars_up)
        print('Каков шаг сдвига?')
        shag = int(input())
        print('Введите сообщение')
        s = input()
        s = list(s)
        for i in range(len(s)):
            if s[i] in chars_up:
                j = chars_up.index(s[i])
                if j-shag >= 0:
                    s[i] = chars_up[j-shag]
                else:
                    s[i] = chars_up[j-shag+26]
            if s[i] in chars_low:
                j = chars_low.index(s[i])
                if j-shag >= 0:
                    s[i] = chars_low[j-shag]
                else:
                    s[i] = chars_low[j-shag+26]
        deshifr = ''.join(s)
        print(deshifr)
    elif y == 'русский' or y == 'russian':
        chars_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        chars_low = list(chars_low)
        chars_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        chars_up = list(chars_up)
        print('Каков шаг сдвига?')
        shag = int(input())
        print('Введите сообщение')
        s = input()
        s = list(s)
        for i in range(len(s)):
            if s[i] in chars_up:
                j = chars_up.index(s[i])
                if j-shag >= 0:
                    s[i] = chars_up[j-shag]
                else:
                    s[i] = chars_up[j-shag+32]
            if s[i] in chars_low:
                j = chars_low.index(s[i])
                if j-shag >= 0:
                    s[i] = chars_low[j-shag]
                else:
                    s[i] = chars_low[j-shag+32]
        deshifr = ''.join(s)
        print(deshifr)
