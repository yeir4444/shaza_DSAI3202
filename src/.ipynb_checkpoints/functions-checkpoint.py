import time
import random
import string
# Function to join a thousand random letters
def join_random_letters(num):
    letters =[random.choice(string.ascii_letters) for _ in range(num)]
    joined_letters = ''.join(letters)
    

# Function to add a thousand random numbers
def add_random_numbers(num):
    numbers = [random.randint(1, 100) for _ in range(num)]
    total_sum = sum(numbers)
    
