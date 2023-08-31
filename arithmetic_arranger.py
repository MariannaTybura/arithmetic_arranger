def arithmetic_arranger(problems, show_results=False):
    if not problems:
        return "Error: There should be minimum one problem"
    elif len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in problems:
        parts = problem.split()
        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]

        len_of_first_number = len(first_number)
        len_of_second_number = len(second_number)
        width = 2 + max(len_of_first_number, len_of_second_number)

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        if not (first_number.isdigit() and second_number.isdigit()):
            return "Error: Numbers must only contain digits."
        if len_of_first_number > 4 or len_of_second_number > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = int(first_number) + int(second_number)
        else:
            result = int(first_number) - int(second_number)
        result = str(result)
        len_of_result = len(result)

        first_line = first_line + " " * (width - len_of_first_number) + first_number + " " * 4
        second_line = second_line + operator + " " * (width - 1 - len_of_second_number) + second_number + " " * 4
        third_line = third_line + "-" * width + " " * 4
        fourth_line = fourth_line + " " * (width - len_of_result) + result + " " * 4

    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()

    arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    if show_results:
        arranged_problems = arranged_problems + "\n" + fourth_line

    return arranged_problems


print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

