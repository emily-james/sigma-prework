num_list = input("Enter integers separated by commas: ").split(',')
int_list = [int(num) for num in num_list]


def max_min(numbers):
    """Sorts to find the minimum and maximum integers in the list. List element with index 0 is the
    minimum value and index -1 is the maximum value.
    Input:
        numbers (list): list of integers
    Returns:
        (list): minimum and maximum integers in numbers list.
        """

    numbers.sort()

    min_num = numbers[0]
    max_num = numbers[-1]

    return [min_num, max_num]


print(max_min(int_list))
