def insertion_sort(A):
    for j in range(1, len(A)): # iterate for the entire sequence
        key = A[j] # set the current element to "key"
        i = j - 1 # set i to the index of the current element minus 1
        # the following loop is used to shift elemets before "key" greater than "key" to the right
        while i >= 0 and A[i] > key: # loop while i is positive and while [condition: next element is greater than the key]
            A[i + 1] = A[i] # 
            i = i - 1
        A[i + 1] = key
    return A

def nonincreasing_insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key: # worst case: runs up to j times.
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def linear_search(A, v):
    for i in range(0,len(A)):
        if A[i] == v:
            return i
    print("NIL")
    return -1

def selection_sort(A):
    sortedList = []
    while len(A) != 0:
        smallestIndex = 0
        for i in range(len(A)):
            if A[i] < A[smallestIndex]:
                smallestIndex = i
        sortedList.append(A.pop(smallestIndex))
    return sortedList

def get_duplicates(A): # runs in O(nlgn) + O(n) = O(nlgn)
    '''Returns a list of elements that are repeated more than once'''
    duplicates = []
    A = selection_sort(A) # this runs O(n^2) or O(nlgn) depending on the sorting algorithm used
    i = 0
    while (i < len(A) - 1): # this runs O(n)
        if A[i] == A[i+1]:
            duplicates.append(A[i])
            i += 1
        i += 1
    return duplicates

def evaluate_polynomial(coefficients, x):
    '''important: write 0 for coefficients for non-existing terms in the polynomial'''
    n = len(coefficients)
    sum = 0
    for i in range(n):
        exponent_term = x**i
        sum += exponent_term*coefficients[i]
    return sum

def evaluate_polynomial_horner(coefficients, x):
    n = len(coefficients)
    sum = coefficients[n-1]
    for i in range(n-2, -1, -1):
        sum = sum*x + coefficients[i]
    return sum

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return (n + recursive_sum(n-1))

def merge(A, p, q, r):
    A1 = A[p:q]
    A2 = A[q:r]
    B = []
    p1 = 0  # Pointer for A1
    p2 = 0  # Pointer for A2
    while (p1 < len(A1)) and (p2 < len(A2)):  # Use 'and' instead of '&'
        if A1[p1] < A2[p2]:
            B.append(A1[p1])
            p1 += 1
        else:
            B.append(A2[p2])
            p2 += 1
    # Append any remaining elements
    B.extend(A1[p1:])
    B.extend(A2[p2:])
    # Replace the sublist in A with B
    A[p:r] = B  # Correct the slicing indices
    return A

def insert(A, a):
    if a <= A[0]:
        return [a] + A
    for i in range(len(A) - 1):
        if A[i] <= a and a <= A[i+1]:
            print(a, "goes between", A[i], "and", A[i+1])
            return A[:i+1] + [a] + A[i+1:]
    return A + [a]

def recursive_insertion_sort(A):
    if len(A) <= 1:
        return A
    else:
        last_element = A.pop()  # Store the last element
        sorted_sublist = recursive_insertion_sort(A)  # Sort the sublist without the last element
        return insert(sorted_sublist, last_element)  # Insert the last element in the sorted sublist

def binary_search(L, a):
    while len(L) > 1:
        m = L[len(L)//2]
        if a == m:
            return L.index(a)
        if a < m:
            L = L[:m+1]
        else:
            L = L[m:]
    return L[0]

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def faster_fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        (a,b) = (0,1)
        for _  in range(2,n+1):
            a,b = b, a + b
        return b

import math as m

def findNumber(steps, i, j):
    interval = abs(i - j)
    smallest = m.inf
    smallest_num = -1
    for x in range(steps):
        num = i + x*(interval/steps)

        left = num
        right = 8*m.log2(num)

        sub = abs(left - right)
        if sub < smallest:
            smallest = sub
            smallest_num = num
    return smallest_num

def find_root(fun, a, b): # binary search, uses positive/negative as check
    minimum = a 
    maximum = b 
    while abs(minimum - maximum) > 1e-8:
        mid = (maximum + minimum)/2
        res = fun(mid)
        if (res * fun(minimum) > 0):
            minimum = mid
        else:
            maximum = mid 
    return minimum


def med_five_elements(A):
    A = sorted(A)
    return A[2]

def median(A):
    if len(A) == 5:
        return med_five_elements(A)
    else:
        new_medians = []
        for i in range(int(len(A)/5)):
            new_medians.append(med_five_elements(A[5*i:5*(i+1)]))
        return median(new_medians)

def merge_sort2(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort2(L)  # Sorting the first half
        merge_sort2(R)  # Sorting the second half

        merge2(arr, L, R)

def merge2(arr, L, R):
    i = j = k = 0

    # Merging the temp arrays back into arr
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def printFun(test):
 
    if (test < 1):
        return
    else:
 
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print(test, end=" ")
        return
 
def fun(n):
    if n > 0: 
        fun(n-1)
        print(n)

def get_binary_ones(n):
    A = []
    A.append(0)
    A.append(1)
    counter = 2
    for i in range(2,n+1):
        if i % counter == 0:
            counter = i
        A.append(A[i - counter] + 1)
    return(A)

def binomial_coefficient(n, k):
    # Base cases
    if k == 0 or k == n:
        return 1
    # Recursive step
    else:
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
    
def binomial_coefficient_dynamic(N, K):
    C = [[0 for _ in range(K+1)] for _ in range(N+1)]
    
    for n in range(N+1):
        for k in range(K+1):
            if k == 0 or k == n:
                C[n][k] = 1
            else:
                C[n][k] = C[n-1][k-1] + C[n-1][k]
    return C[N][K]

N = 5
K = 2
print(f"Binomial Coefficient of ({N}, {K}) is: {binomial_coefficient_dynamic(N, K)}")