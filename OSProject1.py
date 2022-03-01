#John Aningalan
import threading
import time
from numpy import random
#Creating a random integer with a size 21
A = random.randint(100,size=(21))
def split_list(a_list):
    third = len(a_list)//3
    return a_list[0:7], a_list[7:14], a_list[14:21]
#split the array into 3 smaller groups
B, C, D = split_list(A)
a = B
b = C
c = D

def QuickSort(arr):

    elements = len(arr)
    
    
    if elements < 2:
        return arr
    
    current_position = 0 

    for i in range(1, elements):
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = QuickSort(arr[0:current_position]) 
    right = QuickSort(arr[current_position+1:elements]) 

    arr = left + [arr[current_position]] + right 
    
    return arr
#Making a QuickSort Function
def merge_two(a, b):
    (m, n) = (len(a), len(b))
    i = j = 0
 
    # Destination Array
    d = []
 
    # Merge from a and b together
    while i < m and j < n:
        if a[i] <= b[j]:
            d.append(a[i])
            i += 1
        else:
            d.append(b[j])
            j += 1
 
    # Merge from a if b has run out
    while i < m:
        d.append(a[i])
        i += 1
 
    # Merge from b if a has run out
    while j < n:
        d.append(b[j])
        j += 1
 
    return d
 
def merge(a, b, c):
    t = merge_two(a, b)
    return merge_two(t, c)
d = merge(a,b,c)
def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        
        L = arr[:mid]
 
        
        R = arr[mid:]
 
        
        mergeSort(L)
 
        
        mergeSort(R)
 
        i = j = k = 0
 
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
#merge sort function from merging the 3 arrays then mergesorting them back
#using thread 1-3 to sort arrays 1-3
#using thread 4 to combine and mergesort everything
def sortingthread1(num):
    """
    function to print cube of given num
    """
    print("Original Array 1: ",B, "\n")
    QuickSort(a)
    time.sleep(1)
    print("Sorted Array 1: ", a,"\n")
    
def sortingthread2(num):
    """
    function to print cube of given num
    """
    time.sleep(1)
    print("Original Array 2: ",C,"\n")
    QuickSort(b)
    time.sleep(2)
    print("Sorted Array 2: ", b,"\n")
    
def sortingthread3(num):
    """
    function to print cube of given num
    """
    time.sleep(2)
    print("Original Array 3: ",D,"\n")
    QuickSort(c)
    time.sleep(3)
    print("Sorted Array 3: ", c,"\n")
def mergethread4(num):
    time.sleep(3)
    print("Original Merged Array: ",merge(a,b,c),"\n")
    time.sleep(4)
    mergeSort(d)
    print("Merge Sorted Array", d,"\n")
    

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=sortingthread1, args=(10,))
    t2 = threading.Thread(target=sortingthread2, args=(10,))
    t3 = threading.Thread(target=sortingthread3, args=(10,))
    t4 = threading.Thread(target=mergethread4, args=(10,))
    
    
  
    # starting thread
    t1.start()
    t2.start()
    t3.start()
    t4.start()

  
    t1.join()
    t2.join()
    t3.join()
    t4.join()

  
    # to show that everything is done
    print("Done!")



