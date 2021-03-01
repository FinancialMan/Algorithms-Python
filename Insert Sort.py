A = [50, 20000, 1, 88778, 5, 121, 244, 60]

def insert_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j]>key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A

a = insert_sort(A)
print(a)
