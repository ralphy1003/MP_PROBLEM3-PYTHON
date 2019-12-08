#PROBLEM 3-PYTHON
import numpy as np
def PROBLEM3(A):
    for n in range(len(A)):
        B= np.polyfit(A[:,0],A[:,1],n)
        C = np.polyval(B, A[:,0])
        D = np.linalg.norm(A[:,1] - C)
        x = [n,D]
        if n==0:
            y = x
        elif y[1] >= x[1]:
            z = x[0]
    D = np.polyfit(A[:,0],A[:,1],z)
    print('Coefficients: ',D)    
print("nx2 Matrix is needed;hence,the number of rows is needed")
rows = int(input("Enter the number of rows:")) 
columns =2    
print("Please enter the values of the elements of the matrix:")
print("NOTE: Use space when inputting values EX. 1 2 3 4")
VALUES = list(map(int, input().split()))  
MX = np.array(VALUES).reshape(rows, columns)
print("ANSWER:")
PROBLEM3(MX)
