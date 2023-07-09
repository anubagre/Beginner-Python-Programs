#3*3 Magic Square
import numpy
n=3
sq=[]
magic=['_' for i in range(n)]
for i in range(n):
    sq.append(magic)
l=numpy.array(sq)
i,j=n//2,n-1
l[i][j]=1
num=n*n
for x in range(num-1):
    i-=1
    j+=1
    if i==-1 and j==n:
        i,j=0,n-2
    else:
        if i==-1:
            i=n-1
        if j==n:
            j=0
        if l[i][j]!='_':
            i+=1
            j-=2
    l[i][j]=x+2
print("3*3 Magic Square:")
print(numpy.matrix(l))       
            
                
