from typing import Counter


def arithmetic_arranger(problems):
    # this function will take a list of problems and arrange them as they would be arranged by an elementary school student

    # Firstly, let check if the will is less or equal to 5, in the case that it is more than 5 we will raise an error
    try:
        list_size = len(problems)
        if list_size > 5:
            raise ValueError("Error: Too many problems.")
    except ValueError:
        print("Error: Too many problems.")
        return "Error: Too many problems."

    # Now, we loop through our list and we kind do the calculation for all problems and add them in a list
    list_of_results = list()
    list_of_spaces_and_bars = list()

    for problem in problems:
        # What operation is used and it might be just addition or substraction otherwise we raise an error
        operation_symbol = None

        try:
            if "-" in problem:
                operation_symbol = "-"
            if "+" in problem:
                operation_symbol = "+"
            if "*" in problem:
                raise ValueError("Error: Operator must be '+' or '-'.")
            if "/" in problem:
                raise ValueError("Error: Operator must be '+' or '-'.")
        except ValueError:
            print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."

        # We separate the operants in order to clean them and to do the calculation
        operants_holder = problem.split(operation_symbol)

        # we clean our operant by removing all spaces in the beginning and the end
        operants_holder_cleaned = list()
        for operant in operants_holder:
            operants_holder_cleaned.append(operant.strip())

        first_operant = 0
        second_operant = 0

        # Check if the operants are only digits otherwise we raise error
        try:
            first_operant = int(operants_holder_cleaned[0])
        except ValueError:
            print("Error: Numbers must only contain digits")
            return "Error: Numbers must only contain digits"

        try:
            second_operant = int(operants_holder_cleaned[1])
        except ValueError:
            print("Error: Numbers must only contain digits")
            return "Error: Numbers must only contain digits"

        # Check if the operants are only 4 digits long
        if first_operant > 9999 or second_operant > 9999:
            print("Error: Numbers cannot be more than four digits.")
            return "Error: Numbers cannot be more than four digits."

        # Calculating the result of operations
        result = None

        if operation_symbol == "+":
            result = first_operant + second_operant
        if operation_symbol == "-":
            result = first_operant - second_operant

        list_of_results.append(
            [first_operant, second_operant, result, operation_symbol])

        # Calculate space between elements that will be render and the numbers of bars between result and the second operant
        # We will use the operants_holder_cleaned
        # See which of our operants is the longest one
        first_operant_size = len(operants_holder_cleaned[0])
        second_operant_size = len(operants_holder_cleaned[1])

        # Calculate the difference in order to see which one is the longest,
        # if the difference > 0 => the first operant is superior to the second
        # if the difference < 0 => the second operant is superior to the first

        difference = first_operant_size - second_operant_size

        # Calculate the number of bars
        bars_numbers = None

        # if difference < 0, bars numbers = the size of second operant size, and we add the space between the operation symbol and the symbol, which are equals to 2
        if difference < 0:
            difference = difference - 1
            bars_numbers = second_operant_size + 2
        else:
            difference = difference + 1
            bars_numbers = first_operant_size + 2

        list_of_spaces_and_bars.append((difference, bars_numbers))

    # Now, we add space between operators and operants before rendering them
    # In order to do that we have to look for the index of element to know where to add the operator and the second operant so they will be on the same line
    # Here diff = difference and brs = bars_numbers

    index_counter = 0

    for diff, brs in list_of_spaces_and_bars:
        if diff < 0:
            list_of_results[index_counter][3] = list_of_results[index_counter][3] + " "
        else:
            i = 0
            while i < diff:
                list_of_results[index_counter][3] = list_of_results[index_counter][3] + " "
                i += 1
        index_counter += 1

    # Now we calculate bars number for every elements
    bars_list = list()

    for diff, brs in list_of_spaces_and_bars:
        bar_container = ""
        i = 0
        while i < brs:
            bar_container = bar_container + "-"
            i += 1
        bars_list.append(bar_container)

    # Assign elements according to the place it belong
    # this means, we are appending all operants in order to create one complete line that will be returned
    all_first_operants = list()
    all_second_operants = list()
    all_results_list = list()

    # Looping through list of result, adding operator and second operant to the same line
    for result in list_of_results:
        all_first_operants.append(str(result[0]))
        all_second_operants.append(str(result[3]) + str(result[1]))
        all_results_list.append(str(result[2]))

    # Rendering our Elements
    # concatanating all first operants
    first_operant_render = ""

    # Render will contain all elements and will be returned
    render = ""

    # Adding first_operants
    first_checker = 0
    for operant in all_first_operants:
        if first_checker == 0:
            first_operant_render = first_operant_render + \
                "{:>7}".format(operant)
        if first_checker > 0:
            first_operant_render = first_operant_render + \
                "    {:>7}".format(operant)

        first_checker += 1

    render = render + first_operant_render
    render = render + "\n"

    # Adding operators and second operants
    second_operant_render = ""

    second_checker = 0
    for operant in all_second_operants:
        if second_checker == 0:
            second_operant_render = second_operant_render + \
                "{:>7}".format(operant)
        if second_checker > 0:
            second_operant_render = second_operant_render + \
                "    {:>7}".format(operant)

        second_checker += 1

    render = render + second_operant_render
    render = render + "\n"

    # Adding bars
    bars_render = ""

    bars_checker = 0
    for operant in bars_list:
        if bars_checker == 0:
            bars_render = bars_render + \
                "{:>7}".format(operant)
        if bars_checker > 0:
            bars_render = bars_render + \
                "    {:>7}".format(operant)

        bars_checker += 1

    render = render + bars_render

    # Adding the second parameter checker, if it's True we display solutions and if it's False we hide solutions

    print(render)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
