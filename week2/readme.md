while True:

        number = not_number_rejector('Please enter a number: ')

        if low < number and number < high:

            break

    return number
    