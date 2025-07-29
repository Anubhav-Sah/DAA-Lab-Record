import time

def sequential_search(key,arr):
    # Search the key element using sequential search
    # Input-> n number of element, key element which we have to search
    # Output-> index of the key element
    
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        
    return -1


def _main_():
    arr=input('Enter the element of the array using space : ').split()
    
    arr=[int(i) for i in arr]
    
    key=input('Enter the value you want to search : ')
    
    start_time =time.time()
    
    index= sequential_search(key,arr)
    
    end_time= time.time()
    
    print(f"{key} is found in {index+1}position")    
    print(f"Time taken : {end_time-start_time} unit")
    
_main_()
    