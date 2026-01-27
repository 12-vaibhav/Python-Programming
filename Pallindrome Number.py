def is_palindrome(number):
  """
  Checks if a number is a palindrome.

  Args:
    number: The integer to check.

  Returns:
    True if the number is a palindrome, False otherwise.
  """
  # Convert the integer to a string
  # The abs() function handles negative inputs, though palindromes are
  # typically considered in the non-negative context.
  
  num_str = str(abs(number))

  # Check if the string is equal to its reverse.
  # The slicing num_str[::-1] reverses the string.
  return num_str == num_str[::-1]

num1 = 121
num2 = 12345
num3 = 9009
num4 = -121 # The absolute value 121 is a palindrome

print(f"Is {num1} a palindrome? {is_palindrome(num1)}")
print(f"Is {num2} a palindrome? {is_palindrome(num2)}")
print(f"Is {num3} a palindrome? {is_palindrome(num3)}")
print(f"Is {num4} a palindrome? {is_palindrome(num4)}")