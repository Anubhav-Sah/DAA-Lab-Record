# To find the factorial of 'n'number using recurssion
# Input-> n element
# Output-> Factorial of n



import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():

    number = int(input("enter the number:"))

    start_time = time.time()

    result = factorial(number)

    end_time = time.time()

    print(f"Factorial of {number} is {result}")
    print(f"Computation took {end_time - start_time:.8f} seconds")
    