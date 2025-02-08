import random
import string

# Function to join random letters
def join_random_letters(num):
    letters = [random.choice(string.ascii_letters) for _ in range(num)]
    return ''.join(letters)

# Function to add random numbers
def add_random_numbers(num):
    numbers = [random.randint(1, 100) for _ in range(num)]
    return sum(numbers)
