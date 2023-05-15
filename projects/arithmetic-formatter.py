def arithmetic_arranger(problems, result=False):
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for problem in problems:
        operand_left, operator, operand_right = problem.split()

        if operator not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if not operand_left.isdigit() or not operand_right.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(operand_left) > 4 or len(operand_right) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(problems) > 5:
            return 'Error: Too many problems.'
        if operator == '+':
            operation_result = int(operand_left) + int(operand_right)
        else:
            operation_result = int(operand_left) - int(operand_right)

        length = max(len(operand_left), len(operand_right)) + 2

        first_line += operand_left.rjust(length) + '    '
        second_line += operator + operand_right.rjust(length - 1) + '    '
        third_line += '-' * length + '    '
        fourth_line += str(operation_result).rjust(length) + '    '

    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + \
        '\n' + third_line.rstrip()

    if result:
        arranged_problems += '\n' + fourth_line.rstrip()

    return arranged_problems


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
