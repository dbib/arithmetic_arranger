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

        print(operants_holder_cleaned)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
