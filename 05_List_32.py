n = int(input())

curr_que = None
q = []
called = []
sum_dt = 0
count = 0 
while n != 0:
    cmd = input().split()

    if cmd[0] == "reset":
        curr_que = int(cmd[1])
    elif cmd[0] == "new":
        print("ticket {}".format(curr_que))
        q.append(int(cmd[1]))
        curr_que += 1
    elif cmd[0] == "next":
        called = [curr_que-len(q), q[0]]
        print("call {}".format(called[0]))
        q = q[1:]
    elif cmd[0] == "order":
        dt = int(cmd[1]) - called[1]
        print("qtime {} {}".format(called[0], dt))
        sum_dt += dt
        count += 1
    elif cmd[0] == "avg_qtime":
        print("avg_qtime {}".format(sum_dt/count))
    
    n -= 1



