def arithmetic_arranger(problem_list, show_answers=False):
    """Formats a list of addition and subtraction problems
    arranged vertically and side-by-side.
    
    The function will return an error if the list has more than
    five problems or uses operators other than '+' or '-'.
    Numbers must only contain digits and cannot contain more than
    four digits (i.e. cannot be > 9999).

    Parameters
    ----------
    problem_list : list of str
        A list of up to five arithmetric problems.
    show_answers : bool, default=False
        A flag used to print answers to the problems.
    
    Returns
    -------
    str
        A string of 3 rows (4 if show_answers=True) with the problems
        arranged vertically and side-by-side.
        Example:
          32         1      523
        +  8    - 3801    -  49
        ----    ------    -----
          40     -3800      474
    
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
    
# Manipulate data ready for output
    first_row = []
    second_row = []
    third_row = []
    if show_answers:
        answers = []
        fourth_row = []
    for i in range(0, num_of_problems):
        widths.append(max(len(first_numbers[i]), len(second_numbers[i])))
        first_row.append(first_numbers[i].rjust(widths[i] + 2))
        second_row.append(signs[i] + " " + second_numbers[i].rjust(widths[i]))
        third_row.append("-" * (widths[i] + 2))
        if show_answers:
            if signs[i] == "+":
                answers.append(int(first_numbers[i]) + int(second_numbers[i]))
            elif signs[i] == "-":
                answers.append(int(first_numbers[i]) - int(second_numbers[i]))
            fourth_row.append(str(answers[i]).rjust(widths[i] + 2))

# Join everything together and return formatted problems
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
#    help(arithmetic_arranger)
    print('\nList ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"] produces:\n')
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print('\nList ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"] (with show_answers=True) produces:\n')
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
    print()
    
