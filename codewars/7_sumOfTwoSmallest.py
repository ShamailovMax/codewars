def sum_two_smallest_numbers(numbers, summ=0):
    for i in range(2):
        summ = summ + min(numbers)
        numbers.remove(min(numbers))
    return summ
