n = int(input())

if n > 999999999:
    if n > 9999999999:
        print("{}B".format(round(n/1000000000)))
    else:
        print("{}B".format(round(n/1000000000, 1)))
elif n > 999999:
    if n > 9999999:
        print("{}M".format(round(n/1000000)))
    else:
        print("{}M".format(round(n/1000000, 1)))
elif n > 999:
    if n > 9999:
        print("{}K".format(round(n/1000)))
    else:
        print("{}K".format(round(n/1000, 1)))
else:
    print(n)
