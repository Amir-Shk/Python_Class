def fibonacci_series(f):
    """
    This function takes the number of members
    generates a Fibonacci sequence for the number you specified
    """
    fibonacci_sequence = [0 , 1]
    while len(fibonacci_sequence) < f:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence


s = int(input("Enter the number of sequence members : "))

print(fibonacci_series(s))