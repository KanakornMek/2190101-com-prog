n = input()

if n[:2] in ["06", "08", "09"]:
    if len(n) == 10:
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")
