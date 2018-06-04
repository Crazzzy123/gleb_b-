import math


def expression_calculator(expression):
    available_operations = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}

    # Проверка на корректность скобок
    braces = 0
    left_brace = right_brace = -1
    for i in range(len(expression)):
        if expression[i] == '(':
            braces += 1
            left_brace = i
            if i != 0 and expression[i - 1] not in available_operations and expression[i - 1] != '(' and expression[
                i - 1] not in 'nsg':
                return 'Error0'
        elif expression[i] == ')':
            if braces == 0:
                return 'Error0'
            else:
                braces -= 1
                right_brace = i
            if right_brace - left_brace == 1:
                return 'Error0'
            if i != len(expression) - 1 and expression[i + 1] not in available_operations and expression[i + 1] != ')':
                return 'Error0'
    if braces != 0:
        return 'Error0'

    # Упрощение ф-ций
    while expression.find('sin') != -1 or expression.find('cos') != -1 or expression.find(
            'tg') != -1 or expression.find('ctg') != -1:
        if expression.find('sin') != -1:
            start_of_sin_expression = expression.find('sin') + 4
            sin_expression = expression[expression.find('sin'):]
            braces_sin = 0
            for i in range(len(sin_expression)):
                if sin_expression[i] == '(':
                    braces_sin += 1
                elif sin_expression[i] == ')':
                    if braces_sin == 1:
                        end_of_sin_expression = expression.find('sin') + i
                        break
                    else:
                        braces_sin -= 1
            check = discard_square_brackets(
                expression_calculator(expression[start_of_sin_expression: end_of_sin_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.sin(float(check)), 8)
                if check >= 0:
                    if end_of_sin_expression == len(expression) - 1:
                        expression = expression[:start_of_sin_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_sin_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_sin_expression + 1:]
                else:
                    if end_of_sin_expression == len(expression) - 1:
                        expression = expression[:start_of_sin_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_sin_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_sin_expression + 1:]
        elif expression.find('cos') != -1:
            start_of_cos_expression = expression.find('cos') + 4
            cos_expression = expression[expression.find('cos'):]
            braces_cos = 0
            for i in range(len(cos_expression)):
                if cos_expression[i] == '(':
                    braces_cos += 1
                elif cos_expression[i] == ')':
                    if braces_cos == 1:
                        end_of_cos_expression = expression.find('cos') + i
                        break
                    else:
                        braces_cos -= 1
            check = discard_square_brackets(
                expression_calculator(expression[start_of_cos_expression: end_of_cos_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.cos(float(check)), 8)
                if check >= 0:
                    if end_of_cos_expression == len(expression) - 1:
                        expression = expression[:start_of_cos_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_cos_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_cos_expression + 1:]
                else:
                    if end_of_cos_expression == len(expression) - 1:
                        expression = expression[:start_of_cos_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_cos_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_cos_expression + 1:]

        elif expression.find('tg') != -1:
            start_of_tg_expression = expression.find('tg') + 4
            tg_expression = expression[expression.find('tg'):]
            braces_tg = 0
            for i in range(len(tg_expression)):
                if tg_expression[i] == '(':
                    braces_tg += 1
                elif tg_expression[i] == ')':
                    if braces_tg == 1:
                        end_of_tg_expression = expression.find('tg') + i
                        break
                    else:
                        braces_tg -= 1
            check = discard_square_brackets(
                expression_calculator(expression[start_of_tg_expression: end_of_tg_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.tan(float(check)), 8)
                if check >= 0:
                    if end_of_tg_expression == len(expression) - 1:
                        expression = expression[:start_of_tg_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_tg_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_tg_expression + 1:]
                else:
                    if end_of_tg_expression == len(expression) - 1:
                        expression = expression[:start_of_tg_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_tg_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_tg_expression + 1:]

        elif expression.find('ctg') != -1:
            start_of_ctg_expression = expression.find('ctg') + 4
            ctg_expression = expression[expression.find('ctg'):]
            braces_ctg = 0
            for i in range(len(ctg_expression)):
                if ctg_expression[i] == '(':
                    braces_ctg += 1
                elif ctg_expression[i] == ')':
                    if braces_ctg == 1:
                        end_of_ctg_expression = expression.find('ctg') + i
                        break
                    else:
                        braces_ctg -= 1
            check = discard_square_brackets(
                expression_calculator(expression[start_of_ctg_expression: end_of_ctg_expression]))
            if check == 'Error1':
                return 'Error1'
            else:
                check = round(math.tan(float(check)), 8)
                if check > 0:
                    check = 1 / check
                    if end_of_ctg_expression == len(expression) - 1:
                        expression = expression[:start_of_ctg_expression - 4] + str(check)
                    else:
                        expression = expression[:start_of_ctg_expression - 4] + \
                                     str(check) + \
                                     expression[end_of_ctg_expression + 1:]
                elif check < 0:
                    check = 1 / check
                    if end_of_ctg_expression == len(expression) - 1:
                        expression = expression[:start_of_ctg_expression - 4] + '[' + str(check) + ']'
                    else:
                        expression = expression[:start_of_ctg_expression - 4] + \
                                     '[' + str(check) + ']' + \
                                     expression[end_of_ctg_expression + 1:]
                else:
                    return 'Error1'

    # Упрощение скобок
    while '(' in expression:
        flag_left_brace = flag_right_brace = True
        left_brace = right_brace = -1
        braces = 0
        for i in range(len(expression)):
            if flag_left_brace and expression[i] == '(':
                braces += 1
                left_brace = i
                flag_left_brace = False
            elif expression[i] == '(' and right_brace == -1:
                braces += 1
            elif expression[i] == ')' and braces != 0:
                braces -= 1
                if flag_right_brace and braces == 0:
                    right_brace = i
                    flag_right_brace = False
        if check_number(expression[
                        left_brace + 1:right_brace]):  # Если в скобках просто отрицательное число, то меняем круглые скобки на квадратные
            if int(expression[left_brace + 1:right_brace]) < 0:
                expression = expression[:left_brace] + '[' + \
                             expression[left_brace + 1:right_brace] + ']' + \
                             expression[right_brace + 1:]
            else:
                expression = expression[:left_brace] + \
                             expression[left_brace + 1:right_brace] + \
                             expression[right_brace + 1:]
        else:
            check_division = expression_calculator(expression[left_brace + 1:right_brace])
            if check_division == 'Error1':
                return 'Error1'
            else:
                expression = expression[:left_brace] + \
                             check_division + \
                             expression[right_brace + 1:]

    # Поиск максимального приоритета среди введенных операций
    current = -1
    for i in range(len(expression)):
        if expression[i] in available_operations and current < available_operations[expression[i]]:
            if expression[i] == '-' and expression[i - 1] == '[':
                continue
            else:
                current = available_operations[expression[i]]
    if current == -1:
        return expression

    # Вычисление блоков операций с максимальным приоритетом с помощью ф-ции block_calculator
    left = 0  # Индекс операции с меньшим приоритетом, чем максимальный, находящейся слева (левая граница блока)
    result_expression = ''
    first_block = True
    for i in range(len(expression)):
        if expression[i] in available_operations and \
                current > available_operations[expression[i]]:
            if (expression[i] == '-' and expression[i - 1] == '[') or (
                    expression[i] == '-' and expression[i - 1] == 'e'):
                continue
            if first_block:
                block_for_record = block_calculator(expression[left:i])
                if block_for_record == 'Error1':
                    return 'Error1'
                elif block_for_record < 0:
                    result_expression = '[' + str(block_for_record) + ']' + expression[i]  # запись первого блока
                else:
                    result_expression = str(block_for_record) + expression[i]
                first_block = False
            else:
                block_for_record = block_calculator(expression[left:i])
                if block_for_record == 'Error1':
                    return 'Error1'
                elif block_for_record < 0:
                    result_expression += '[' + str(block_for_record) + ']' + expression[i]  # запись первого блока
                else:
                    result_expression += str(block_for_record) + expression[i]
            left = i + 1
        elif left != 0 and i == len(expression) - 1:
            block_for_record = block_calculator(expression[left:])
            if block_for_record == 'Error1':
                return 'Error1'
            elif block_for_record < 0:
                result_expression += '[' + str(block_for_record) + ']'
            else:
                result_expression += str(block_for_record)
    if left == 0:
        block_for_record = block_calculator(discard_square_brackets(expression))
        if block_for_record == 'Error1':
            return 'Error1'
        elif block_for_record < 0:
            result_expression = '[' + str(block_for_record) + ']'
        else:
            result_expression = str(block_for_record)

    # Проверка того, что получен конечный ответ, если нет, то продолжить вычисление
    if check_number(result_expression):
        return result_expression
    else:
        check_division = expression_calculator(result_expression)
        if check_division == 'Error1':
            return 'Error1'
        else:
            return check_division


def block_calculator(expression):
    # Если expression - число, то вернуть его,
    # если нет, то вычислить выражение, содержащее операции одного приоритета
    if check_number(discard_square_brackets(expression)):
        return float(discard_square_brackets(expression))
    else:
        flag_first = True
        left = 0
        available_operations = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}
        if expression.find('^') > 0:
            return exponentiation(expression)
        for i in range(len(expression)):
            if (expression[i] == '-' and i != 0 and expression[i - 1] == '[') or (expression[i] == '-' and expression[
                i - 1] == 'e'):  # Если встретили минус, как знак числа, то пропустим его
                continue
            elif flag_first and expression[i] in available_operations:  # Запись первого числа в result
                result = float(discard_square_brackets(expression[left:i]))
                flag_first = False
                left = i
            elif expression[i] in available_operations:  # вычисление операции, если кончился второй операнд
                if expression[left] == '+':
                    result += float(discard_square_brackets(expression[left + 1:i]))
                    left = i
                elif expression[left] == '-':
                    result -= float(discard_square_brackets(expression[left + 1:i]))
                    left = i
                elif expression[left] == '*':
                    result *= float(discard_square_brackets(expression[left + 1:i]))
                    left = i
                elif expression[left] == '/':
                    check_division = float(discard_square_brackets(expression[left + 1:i]))
                    if check_division != 0:
                        result /= check_division
                    else:
                        return 'Error1'
                    left = i
            elif i == len(expression) - 1:  # вычисление операции, если она последняя
                if expression[left] == '+':
                    result += float(discard_square_brackets(expression[left + 1:]))
                elif expression[left] == '-':
                    result -= float(discard_square_brackets(expression[left + 1:]))
                elif expression[left] == '*':
                    result *= float(discard_square_brackets(expression[left + 1:]))
                elif expression[left] == '/':
                    check_division = float(discard_square_brackets(expression[left + 1:]))
                    if check_division != 0:
                        result /= check_division
                    else:
                        return 'Error1'
        return result


def exponentiation(expression):
    k = expression.find('^')
    if k > 0:
        return float(discard_square_brackets(expression[:k])) ** exponentiation(expression[k + 1:])
    else:
        return float(discard_square_brackets(expression))


def check_number(expression, flag=False):
    available_numbers = '0123456789.'
    for i in range(len(expression)):
        if expression[i] == '-' and i == 0:
            continue
        elif flag and expression[i] in '[]':
            continue
        elif expression[i] not in available_numbers:
            return False
    return True


def discard_square_brackets(expression):
    if 'e' in expression:
        expression = expression[:expression.find('e')] + '^' + expression[expression.find('e') + 1:]
    if len(expression) > 3 and expression[0] == '[' and expression[-1] == ']':
        return discard_square_brackets(expression[1:-1])
    return expression


def pls_help_me():
    print("""
    Добро пожаловать в интерпретатор математических выражений!
    В данной программе вы можете ввести математическое выражение и
    получить результат его вычисления.

    Интерпретатор понимает использование следующих символов:
        + - * / ^ ( )
    А также вы можете использовать следующие математические функции:
        sin() cos() tg() ctg()

    Пример корректного выражения:
    (10-15)*(20-19)/(15-10)+11    
    """)


def check_expression(expression):
    available_symbols = '+-/*^()sct0123456789.'
    available_operations = '+-*/^'
    available_right = '0123456789sct('
    available_left = '0123456789)'
    available_numbers = '0123456789'
    i = 0
    while i < len(expression):
        if expression[i] in available_symbols:
            if expression[i] == 's':
                if expression[i + 1:i + 4] == 'in(':  # Проверка, что 's' часть 'sin('
                    i += 4
                else:
                    return False
            elif expression[i] == 'c':
                if expression[i + 1:i + 4] == 'os(':  # Проверка, что 'c' часть 'cos('
                    i += 4
                elif expression[i + 1:i + 4] == 'tg(':  # Проверка, что 'c' часть 'ctg('
                    i += 4
                else:
                    return False
            elif expression[i] == 't':  # Проверка, что 't' часть 'tg('
                if expression[i + 1:i + 3] == 'g(':
                    i += 3
                else:
                    return False
            elif expression[i] in available_operations:
                if i == 0 or i == len(expression) - 1 or \
                        expression[i - 1] not in available_left or \
                        expression[i + 1] not in available_right:
                    return False
            elif expression[i] == '.':
                if expression[i - 1] not in available_numbers or expression[i + 1] not in available_numbers:
                    return False
            i += 1
        else:
            return False
    return True


def delete_spaces(expression):
    expression = expression.strip()
    count_spaces = i = 0
    while i < len(expression) - count_spaces:
        if expression[i] == ' ':
            count_spaces += 1
            expression = expression[:i] + expression[i + 1:]
        i += 1
    return expression


def replace_x(expression, value):
    if value >= 0:
        while expression.find('x') != -1:
            expression = expression[:expression.find('x')] + str(value) + expression[expression.find('x') + 1:]
    else:
        while expression.find('x') != -1:
            expression = expression[:expression.find('x')] + '[' + str(value) + ']' + expression[expression.find('x') + 1:]
    return expression


def start_calculate(expression, start, end, step):
    set_y = []
    current_value = start
    expression = delete_spaces(expression)
    while current_value <= end+step:
        set_y.append(round(float(discard_square_brackets(expression_calculator(replace_x(expression, current_value)))), 8))
        current_value += step
    return set_y