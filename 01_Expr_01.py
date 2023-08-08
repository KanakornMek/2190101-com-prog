import math
sqrt = math.sqrt
pi = math.pi
e = math.e

n = int(input())

print(sqrt(2*pi)*(n**(n+1/2))*(e**(-n+(1/(12*n+1)))))
print(sqrt(2*pi)*(n**(n+1/2))*(e**(-n+(1/(12*n)))))