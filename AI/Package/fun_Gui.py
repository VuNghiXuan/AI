import pygame

# Tìm tọa độ 3 điểm còn lại của hình chữ nhật, 
#       khi cho trước tọa độ 1 điểm và chiều dài, chiều rộng


def fun_poss_three_rectangular_points(point_A, rect_width, rect_height):
    # three_hCN = fun_poss_three_rectangular_points((50,50), 700,500)
    "point_A = tupe(xA,yA)" 
    "rect_width: Chiều rộng hcn là cạnh AB"
    " A __________ B"
    "  |          |  "
    " D __________ C"
    "rect_height: Chiều cao hcn là cạnh BC"
    xA = point_A[0]
    yA = point_A[1]

    # tính tọa độ điểm B
    xB = point_A[0] + rect_width
    yB = yA

    # tính tọa độ điểm C
    xC = xB
    yC = yA + rect_height

    # tính tọa độ điểm D
    xD = xA
    yD = yC
    return (xA, yA), (xB, yB), (xC, yC), (xD, yD)

def fun_create_text(in_str):
    white = (255, 255, 255)
    font = pygame.font.SysFont('sans', 40)
    out_str = font.render(in_str, True, white) # render: hiển thị (bề mặt)
    return out_str