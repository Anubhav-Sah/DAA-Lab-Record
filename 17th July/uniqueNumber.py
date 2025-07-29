# TO find the unique number in Array
# Input-> n number of element of Array
# Output-> Unique number of Array 

import time


def uniqueElement(arr):
    
    
    
    uniqueElement=[]
    for i in arr:
        count=arr.count(i)
        
        if count==1:
            uniqueElement.append(i)
    
    return uniqueElement


def main():
    arr=input("Enter the element of the array using space : ").split()
    start=time.time()
    arr=[int(i) for i in arr]
    
    print(f"Unique element of the array : {uniqueElement(arr)}")
    end=time.time()
    print(f"Total time taken by algorithm is {(end-start):.8f} sec")
    
main()