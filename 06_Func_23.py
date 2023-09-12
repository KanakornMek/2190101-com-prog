def make_int_list(x:str):
    return [int(a) for a in x.split()]
def is_odd(e):
    if e % 2 == 0:
        return False
    return True
def odd_list(alist):
    odd_ls = []
    for i in alist:
        if is_odd(i):
            odd_ls.append(i)
     
    return odd_ls
def sum_square(alist):
    sum = 0
    for i in alist:
        sum += i**2
    return sum

exec(input().strip())
