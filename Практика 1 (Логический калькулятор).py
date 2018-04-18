print("Двойка в качестве знака операции завершит работу программы")
print("Вводите 1 или 0")
while True:
        s = input("Выберите знак операции (and,or,+): ")
        if s == '2': break
        if s in ('and','or','+'):
                x = input("x=")
                y = input("y=")
                if (((x!=0) and (x!=1)) or ((y!=0) and (y!=1))):
                    continue
                if s == 'and':
                    if (x==1) and (y==1):
                        print("1")
                    else:
                        print("0")
                elif s == 'or':
                    if (x==0) and (y==0):
                        print("0")
                    else:
                        print("1")
                elif s == '+':
                    if (x == y):
                        print("0")
                    else:
                        print("1")
        else:
            print("Неверный знак")
