def is_armstrong(number):
    """
    Checks if a given number is an Armstrong number.

    """
    
    # Convert the number to a string to easily find the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Initialize the sum of powers
    sum_of_powers = 0
    
    # Iterate through each digit in the string
    for digit in num_str:
        # Convert the character digit back to an integer and raise it to the power of num_digits
        sum_of_powers += int(digit) ** num_digits
        
    # Check if the calculated sum is equal to the original number
    if sum_of_powers == number:
        return True
    else:
        return False

# Main part of the script to take input and run the function
if __name__ == "__main__":
    # Take input from the user
    try:
        user_input = int(input("Enter a number to check if it is an Armstrong number: "))
        
        # Call the function and print the result
        if is_armstrong(user_input):
            print(f"{user_input} is an Armstrong number.")
        else:
            print(f"{user_input} is not an Armstrong number.")
            
    except ValueError:
        print("Invalid input. Please enter an integer.")

