# To compute the sum of all the element present in Array
# Input->  n number of element present in array
# Output-> sum of all the element present in array
import time
start=0
end=0
def sumofArray(arr):
    start = time.time()
    sum=0
    for i in arr:
        sum+=i 
    end = time.time()
    return sum   

def main():
    arr=input("Enter the element of the array using space : ").split()
    
    arr=[int(i) for i in arr]
    print(f"Sum of all the element of the array : {sumofArray(arr)}")
    print(f"Total time taken by algorithm is {end-start} sec")
    
main()