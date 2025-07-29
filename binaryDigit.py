import time

def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def __main__():
    number = int(input("Enter the number:"))

    start_time = time.time()
    binary_representation = decimal_to_binary(number)
    end_time = time.time()


    if number == 0:
        binary_representation = "0"

    print(f"Decimal: {number}")
    print(f"Binary: {binary_representation}")
    print(f"Time taken: {end_time - start_time} seconds")
    
    
__main__() 