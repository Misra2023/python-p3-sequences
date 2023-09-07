# sequences.py

# Import any necessary modules here

def print_fibonacci(n):
    # Initialize the Fibonacci sequence with the first two terms
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the n-th term
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    # Print the generated Fibonacci sequence
    print(fibonacci_sequence)

# Sample operations on different types of sequences
if __name__ == "__main__":
    # Test the print_fibonacci() function
    print("Fibonacci Sequence:")
    print_fibonacci(9)

    # Sample list operations
    my_list = [1, 2, 3, 4]
    print("List Operations:")
    print(my_list[0])        # Accessing an element by index
    print(my_list[1:3])      # Slicing a list
    print(my_list + [5, 6])  # Concatenating lists

    # Sample tuple operations
    my_tuple = (1, 2, 3, 4)
    print("Tuple Operations:")
    print(my_tuple[2])       # Accessing an element by index

    # Sample range operations
    my_range = range(1, 5)
    print("Range Operations:")
    for num in my_range:
        print(num)

    # Sample string operations
    my_string = "Hello, World!"
    print("String Operations:")
    print(my_string[0])      # Accessing a character by index
    print(my_string.upper()) # Converting to uppercase

    # You can add more operations and tests as needed
