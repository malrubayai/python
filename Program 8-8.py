# This program calculates the total of the values
# in the list.

def main():
    # Create a list.
    numbers = [2, 4, 6, 8, 10]

    # Create a varibale to use as an accumulator.
    total = 0

    # Calculate the total of the list elements.
    for value in numbers:
        total += value

    # Display the total of the list elements.
    print('The total of the elements is', total)

# Call the mian function.
main()
