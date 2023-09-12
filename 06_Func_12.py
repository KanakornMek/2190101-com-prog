def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    while True:
        N += 1
        if is_prime(N):
            return N

def next_twin_prime(N):
    while True:
        N+=1
        if is_prime(N):
            next_prnum = next_prime(N)
            if next_prnum - N == 2:
                return (N, next_prnum)

exec(input().strip())