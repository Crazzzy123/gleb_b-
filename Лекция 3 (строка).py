def f(stroka):
    dic = {}
    for letter in stroka:
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1
    k = 0
    s = ''
    for key in dic.keys():
        s += str(key) + ' : ' + str(dic[key]) + ',  '
        if k == 5:
            k = 0
            print(s)
            s = ''
        else:
            k += 1


def main():
    stroka = input('Введите строку:')
    f(stroka)


if __name__ == '__main__':
    main()