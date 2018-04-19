import random


def turn_m(matr, d):
    matr_copy = [[0 for i in range(len(matr))] for j in range(len(matr))]
    if d:
        for i in range(len(matr)):
            for j in range(len(matr)):
                matr_copy[i][j] = matr[j][len(matr) - i - 1]
    else:
        for i in range(len(matr)):
            for j in range(len(matr)):
                matr_copy[i][j] = matr[len(matr) - j - 1][i]
    return matr_copy


def print_m(matr):
    for line in matr:
        print(' '.join(line))
    print()


def main():
    n = int(input('Введите размер матрицы:'))
    matr = [[str(random.randrange(100)) for i in range(n)] for j in range(n)]
    print_m(matr)
    print('Поворот матрицы на 90 против часовой:')
    print_m(turn_m(matr, True))
    print('Поворот матрицы на 90 по часовой:')
    print_m(turn_m(matr, False))


if __name__ == '__main__':
    main()
