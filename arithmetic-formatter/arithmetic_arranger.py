def arithmetic_arranger(problem_list, show_answers=False):
    """Formats a list of arithmetic problems arranged vertically and side-by-side.
    
    """
    
    first_numbers = []
    signs = []
    second_numbers = []
    widths = []

# Check input for correct format
    num_of_problems = len(problem_list)
    if num_of_problems > 5:
        return "Error: Too many problems."
    for problem in problem_list:
        parts = problem.split()
        first_numbers.append(parts[0])
        signs.append(parts[1])
        second_numbers.append(parts[2])
    for number in first_numbers + second_numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
        if len(number) > 4:
            return "Error: Numbers cannot be more than four digits."
    for sign in signs:
        if sign not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
    
    first_row = []
    second_row = []
    third_row = []
    if show_answers:
        answers = []
        fourth_row = []

    for i in range(0, num_of_problems):
        if show_answers:
            if signs[i] == "+":
                answers.append(int(first_numbers[i]) + int(second_numbers[i]))
            elif signs[i] == "-":
                answers.append(int(first_numbers[i]) - int(second_numbers[i]))
            widths.append(max(len(first_numbers[i]), len(second_numbers[i]),
                              len(str(answers[i]))))
            fourth_row.append(str(answers[i]).rjust(widths[i] + 2))
        else:
            widths.append(max(len(first_numbers[i]), len(second_numbers[i])))
        first_row.append(first_numbers[i].rjust(widths[i] + 2))
        second_row.append(signs[i] + " " + second_numbers[i].rjust(widths[i]))
        third_row.append("-" * (widths[i] + 2))

    spacer = " " * 4   
    row1 = spacer.join(first_row)
    row2 = spacer.join(second_row)
    row3 = spacer.join(third_row)
    formatted_problems = row1 + "\n" + row2 + "\n" + row3
    if show_answers:
        row4 = spacer.join(fourth_row)
        formatted_problems = formatted_problems + "\n" + row4

    return formatted_problems


if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2", "2 - 1"]))
    print(arithmetic_arranger(["32g + 698", "3801 - 2"]))
    print(arithmetic_arranger(["32 + 698", "38501 - 2"]))
    print(arithmetic_arranger(["32 + 698", "3501 x 2"]))
    print(arithmetic_arranger(["3672 + 6948", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["3672 + 6948", "3801 - 2", "45 + 43", "123 + 49"], True))
    