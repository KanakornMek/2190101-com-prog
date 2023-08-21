import math
a,b,c = input().split(",")

da,db,dc = len(a), len(b), len(c)

numer = int(a+b+c) - int(a+b)
deno = 10**(db+dc) - 10**db

gcd = math.gcd(numer, deno)

print("{} / {}".format(numer//gcd,deno//gcd))