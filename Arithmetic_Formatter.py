def arithmetic_arranger(problems, show_answers=False):
    error_encountered = 0 # max 5
    error_operator = False
    error_digit = False
    error_numbers_of_digits = False
    dictionary = "0123456789"
    unacceptable_operators = ["*", "/"]

    # Per ogni elemento contenuto nella lista problems, spacchetto il primo e il secondo numero e l'operatore
    first_numbers = []
    second_numbers = []
    dashes = []
    third_numbers = []
    for problem in problems:
        parts = problem.split()
        
        # Check if the first operand is too long
        if len(parts[0]) > 4:
            error_numbers_of_digits = True
            print('Error: Numbers cannot be more than four digits.')
            error_encountered += 1
        if not all(char in dictionary for char in parts[0]):
            error_digit = True
            print('Error: Numbers must only contain digits.')
            error_encountered += 1
        #else:
        #    first_numbers.append(parts[0])
        
        # Check if the operator is valid
        if parts[1] in unacceptable_operators:
            error_operator = True
            print("Error: Operator must be '+' or '-'.")
            error_encountered += 1
        #else:
        #    operators.append(parts[1])
        
        # Check if the second operand is too long
        if len(parts[2]) > 4:
            error_numbers_of_digits = True
            print('Error: Numbers cannot be more than four digits.')
            error_encountered += 1
        if not all(char in dictionary for char in parts[2]):
            error_digit = True
            print('Error: Numbers must only contain digits.')
            error_encountered += 1
        #else:
        #    second_numbers.append(parts[2])
        
        max_length = max(len(parts[0]), len(parts[2])) + 2 # +2 for the operator and the space
        first_numbers.append(parts[0].rjust(max_length))
        second_numbers.append(parts[1] + parts[2].rjust(max_length-1))
        dashes.append('-' * max_length)
        if parts[1] == '+':
            third_numbers.append(str(int(parts[0]) + int(parts[2])).rjust(max_length))
        elif parts[1] == '-':
            if int(parts[0]) - int(parts[2]) > 0:
                third_numbers.append(str(int(parts[0]) - int(parts[2])).rjust(max_length))
            else:
                third_numbers.append((parts[1] + str(int(parts[2]) - int(parts[0]))).rjust(max_length-1))
        
        first_numbers.append('    ')
        second_numbers.append('    ')
        dashes.append('    ')
        third_numbers.append('    ')
        
    first_string = ''.join(first_numbers)
    second_string = ''.join(second_numbers)
    dashes_string = ''.join(dashes)
    third_string = ''.join(third_numbers)
    
    string_with_answer = first_string + '\n' + second_string + '\n' + dashes_string + '\n' + third_string

    string_without_answer = first_string + '\n' + second_string + '\n' + dashes_string
    
    if error_encountered < 5:
        if error_operator:
            return "Error: Operator must be '+' or '-'."
        elif error_digit:
            return "Error: Numbers must only contain digits."
        elif error_numbers_of_digits:
            return "Error: Numbers cannot be more than four digits."
        
        if show_answers:
            return string_with_answer
        else:
            return string_without_answer
    else:
        return "Error: Too many problems."

#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

#operation = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
#operation_1 = ["3801 - 2", "123 + 49"]
#operation_2 = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
#operation_3 = ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
#operation_6 = ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
operation_8 = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(operation_8, False))