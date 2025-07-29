# To find the largest element in array
# Input-> n number of element in array
# Output-> largest element in array

import time

start=0
end=0

small=0
def largestNumber(arr):
    start=time.time()
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]<arr[j]:
                small=arr[j]
                print(f"Inside J {arr}")
            arr[i],arr[j]= arr[j],arr[i]
            print(f"Inside i {arr}")
    end=time.time()
    return arr[0]

def main():
    arr=input("Enter the element of the array using space : ").split()
    
    arr=[int(i) for i in arr]
    
    print(f"Largest element of the array : {largestNumber(arr)}")
    print(f"Total time taken by algorithm is {(end-start):.8f} sec")


main()