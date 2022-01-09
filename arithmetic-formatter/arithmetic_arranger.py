def arithmetic_arranger(problem_list, show_answers=False):
    """Formats a list of arithmetic problems arranged vertically and side-by-side.
    
    """
    
    num_of_problems = len(problem_list)
    if num_of_problems > 5:
        return "Error: Too many problems."
    first_numbers = []
    signs = []
    second_numbers = []
    widths = []
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
    if show_answers:
        answers = []
        for x in range(0, num_of_problems):
            if signs[x] == "+":
                answers.append(int(first_numbers[x]) + int(second_numbers[x]))
            elif signs[x] == "-":
                answers.append(int(first_numbers[x]) - int(second_numbers[x]))
        widths.append(max(len(first_numbers[x]), len(second_numbers[x]), len(str((answers[x])))))
    else:
        for x in range(0, num_of_problems):
            widths.append(max(len(first_numbers[x]), len(second_numbers[x])))
    


    
if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2", "2 - 1"]))
    print(arithmetic_arranger(["32g + 698", "3801 - 2"]))
    print(arithmetic_arranger(["32 + 698", "38501 - 2"]))
    print(arithmetic_arranger(["32 + 698", "3501 x 2"]))
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))