def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

def distance2(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)

def distance3(c1, c2):
    dis = ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**(1/2)

    if c1[2]+c2[2] < dis:
        return (dis,False)
    return (dis, True)

def perimeter(points):
    sum_perimeter = 0
    for i in range(1, len(points)):
        sum_perimeter += distance2(points[i-1], points[i])
    sum_perimeter += distance2(points[0], points[-1])
    return sum_perimeter
    
exec(input().strip())