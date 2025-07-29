import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(terms):
    for i in range(terms):
        print(fibonacci(i), end=' ')
    print()

def main():
    num = int(input("Enter a number: "))

    start_time = time.time()
    print_fibonacci_sequence(num)
    end_time = time.time()

    print(f"\nTime taken: {end_time - start_time:.8f} seconds")
    
main()