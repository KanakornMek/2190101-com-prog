u = input()
v = input()

u = u.strip("[]")
v = v.strip("[]")

u = u.split(",")
v = v.split(",")

sum = [0, 0, 0];
for i in range(3):
    u[i] = float(u[i])
    v[i] = float(v[i])
    sum[i] = u[i] + v[i]
print("{} + {} = {}".format(u,v,sum))
