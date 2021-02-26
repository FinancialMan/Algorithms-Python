
A = [1, 2, 4, 6, 9, 12, 15, 17]
p = 1
r = len(A)
x = 4

def binear_searching_recursion(A, p, r, x):
  
    if p>r:
        return 'No found'
    else:
        q = (p + r) // 2
        #print(q)
        if A[q] == x:
            return q
        elif A[q] > x:
            return binear_searching_recursion(A, p, q-1, x)
        elif A[q] < x:
            return binear_searching_recursion(A, q+1, r, x)
        
        
        
a = binear_searching_recursion(A, p, r, x)   