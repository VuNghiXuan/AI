import math

# Tính khoảng cách 2 điểm
def fun_distance(P1, P2):
    dist_x = P1[0]-P2[0]
    dist_y = P1[1]-P2[1]
    dist_xy = math.sqrt((dist_x*dist_x) + (dist_y*dist_y))
    return dist_xy