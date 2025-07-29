import time

def bubble_sort(arr):
    #sort the element using bubble sort
    #INput-> n number of element
    #Output-> Sorted array
    
    
    while(True):
        swapped=False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[(i)]:
                arr[i-1],arr[i]=arr[i],arr[i-1]
                swapped=True
        if not swapped:
            break
    return arr


def _main_():
    arr=input("Enter the element of the array using space : ").split()
    
    arr=[int(i) for i in arr]
    
    start_time=time.time()
    sorted_array=bubble_sort(arr)
    end_time=time.time()        
    print(f"Sorted array : {sorted_array}")
    print(f"Total time taken : {end_time-start_time:.8f} units")
    
    
_main_()