

import pygame
from Package.fun_Gui import fun_create_text, fun_poss_three_rectangular_points
from Package.fun_math import fun_distance
from random import randint



# Tạo Gui
pygame.init()

pygame.display.set_caption('VuNghiXuan_AI')

wight_group = 1200
heigh_group = 700
screen = pygame.display.set_mode([wight_group, heigh_group])

running = True
clock = pygame.time.Clock()

background = (214, 214, 214)
# black = (0, 0, 0) # Đường viền đen
background_panel = (250, 255, 230) # màu panel 
white = (255, 255, 255)

black = (0, 0, 0) 
red = (255, 0, 0) 
green = (0, 255, 0) 
blue = (0, 0, 255) 
yellow = (255, 255, 0) 
turquoise = (0, 255, 255) 
pink = (255, 0, 255)
violet = (81, 31, 144) 

colors = ['red', 'green', 'blue', 'yellow', 'turquoise', 'pink', 'violet']

# tạo text render: hiển thị (bề mặt)
text_plus = fun_create_text("+")
text_minus = fun_create_text("-")
text_K = fun_create_text("K= ")
text_run = fun_create_text("Run")
text_random = fun_create_text("Random")
text_Algorithm = fun_create_text("Algorithm")
text_Reset = fun_create_text("Reset")

K = 0
points =[]
int_errs = 0
clusters = []
labels = []


#  Tọa độ HCN_interface (55, 55, 690, 490))  : Viền đen
pos_A_interface =(50,50)
wight_rect_interface = 700
hieght_rect_interface = 500
rect_interface_xy_A,  rect_interface_xy_B, rect_interface_xy_C, rect_interface_xy_D = fun_poss_three_rectangular_points(pos_A_interface, wight_rect_interface, hieght_rect_interface)

#  Tọa độ HCN_panel (55, 55, 690, 490))
pos_A_penel =(55,55)
wight_rect_penel = 690
hieght_rect_penel = 490
rect_penel_xy_A,  rect_penel_xy_B, rect_penel_xy_C, rect_penel_xy_D = fun_poss_three_rectangular_points(pos_A_penel, wight_rect_penel, hieght_rect_penel)

#  Tọa độ HCN_text plus (850, 50, 50, 50))
pos_A_plus =(850,70)
wight_rect_plus = 50
hieght_rect_plus = 50
rect_plus_xy_A,  rect_plus_xy_B, rect_plus_xy_C, rect_plus_xy_D = fun_poss_three_rectangular_points(pos_A_plus, wight_rect_plus, hieght_rect_plus)

#  Tọa độ HCN text minus (950, 50, 50, 50))
pos_A_minus =(950, 70)
wight_rect_minus = 50
hieght_rect_minus = 50
rect_minus_xy_A,  rect_minus_xy_B, rect_minus_xy_C, rect_minus_xy_D = fun_poss_three_rectangular_points(pos_A_minus, wight_rect_minus, hieght_rect_minus)

#  Tọa độ HCN text K (950, 50, 50, 50))
pos_text_K =(1050, 70)

#  Tọa độ HCN_text run (850, 150, 100, 50))
pos_A_run =(850, 150)
wight_rect_run = 100
hieght_rect_run = 50
rect_run_xy_A,  rect_run_xy_B, rect_run_xy_C, rect_run_xy_D = fun_poss_three_rectangular_points(pos_A_run, wight_rect_run, hieght_rect_run)

#  Tọa độ HCN text random (850, 250, 150, 50))
pos_A_random =(850, 230)
wight_rect_random = 150
hieght_rect_random = 50
rect_random_xy_A,  rect_random_xy_B, rect_random_xy_C, rect_random_xy_D = fun_poss_three_rectangular_points(pos_A_random, wight_rect_random, hieght_rect_random)

#  Tọa độ HCN text Erros (950, 50, 50, 50))
pos_text_Erros =(850, 310)

#  Tọa độ HCN text Algorithm (850, 350, 100, 50))
pos_A_Algorithm =(850, 390)
wight_rect_Algorithm = 150
hieght_rect_Algorithm = 50
rect_Algorithm_xy_A,  rect_Algorithm_xy_B, rect_Algorithm_xy_C, rect_Algorithm_xy_D = fun_poss_three_rectangular_points(pos_A_Algorithm, wight_rect_Algorithm, hieght_rect_Algorithm)

#  Tọa độ HCN text Reset (850, 450, 150, 50))
pos_A_Reset =(850, 470)
wight_rect_Reset = 150
hieght_rect_Reset = 50
rect_Reset_xy_A,  rect_Reset_xy_B, rect_Reset_xy_C, rect_Reset_xy_D = fun_poss_three_rectangular_points(pos_A_Reset, wight_rect_Reset, hieght_rect_Reset)



while running:
    clock.tick(60)    
    screen.fill(background)

    # Vẽ interface
    # pygame.draw.rect(screen, black, (50, 50, 700, 500))
    pygame.draw.rect(screen, black, (pos_A_interface[0],pos_A_interface[1],wight_rect_interface, hieght_rect_interface))

    # Draw panel
    pygame.draw.rect(screen, background_panel, (pos_A_penel[0],pos_A_penel[1],wight_rect_penel, hieght_rect_penel))

    # Draw hcn text_plus    
    pygame.draw.rect(screen, black, (pos_A_plus[0], pos_A_plus[1], wight_rect_plus, hieght_rect_plus))
    screen.blit(text_plus, pos_A_plus) # phương thức blit: Vẽ nhiều bề mặt lên Bề mặt này

    # Draw hcn text_minus
    pygame.draw.rect(screen, black, (pos_A_minus[0], pos_A_minus[1], wight_rect_minus, hieght_rect_minus))
    screen.blit(text_minus, pos_A_minus)    

    # Draw hcn text_K    
    font_K = pygame.font.SysFont('sans', 40)
    text_K = font_K.render("K = " + str(K), True, black)
    screen.blit(text_K, pos_text_K) 

    # Draw hcn text_Run
    pygame.draw.rect(screen, black, (pos_A_run[0], pos_A_run[1], wight_rect_run, hieght_rect_run))
    screen.blit(text_run, pos_A_run)

    # Draw hcn text_random
    pygame.draw.rect(screen, black, (pos_A_random[0], pos_A_random[1], wight_rect_random, hieght_rect_random))
    screen.blit(text_random, pos_A_random)

    # Draw hcn text_Erros  
    font_err = pygame.font.SysFont('sans', 40)
    text_Erros = font_err.render("Erros = " + str(int_errs), True, black)
    screen.blit(text_Erros, pos_text_Erros) 

    # Draw hcn text_Algorithm
    pygame.draw.rect(screen, black, (pos_A_Algorithm[0], pos_A_Algorithm[1], wight_rect_Algorithm, hieght_rect_Algorithm))
    screen.blit(text_Algorithm, pos_A_Algorithm)

    # Draw hcn text_Reset
    pygame.draw.rect(screen, black, (pos_A_Reset[0], pos_A_Reset[1], wight_rect_Reset, hieght_rect_Reset))
    screen.blit(text_Reset, pos_A_Reset)

    
    # Tọa độ mouse
    x_mouse, y_mouse = pygame.mouse.get_pos()

    # Tọa độ quy đổi trong display interface
    x_mouse_face = x_mouse-50
    y_mouse_face = y_mouse-50

    # Tìm vị trí mouse penel
    if x_mouse >= rect_interface_xy_A[0] and x_mouse <= rect_interface_xy_B[0] and y_mouse >= rect_interface_xy_A[1] and y_mouse <= rect_interface_xy_C[1]:
        
        
        
        font_interface = pygame.font.SysFont('sans', 15)
        text_interface = font_interface.render(f'(x: {x_mouse_face}, y: {y_mouse_face})', True, blue)
        screen.blit(text_interface, (x_mouse +12, y_mouse + 12)) 
        # print ("Chuột nằm trong interface", x_mouse, y_mouse) 
    
    # Tương tác nút thoát x đỏ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x_mouse >= rect_interface_xy_A[0] and x_mouse <= rect_interface_xy_B[0] and y_mouse >= rect_interface_xy_A[1] and y_mouse <= rect_interface_xy_C[1]:

                "Xóa đi label để màu để thêm point mới"
                labels = [] # Xử lý lỗi khi chương trình chạy xong mà thêm 1 point nữa
                
                point = [x_mouse_face, y_mouse_face]
                points.append(point)
                # print (points)

            # Tìm vị trí mouse K+    
            if x_mouse >= rect_plus_xy_A[0] and x_mouse <= rect_plus_xy_B[0] and y_mouse >= rect_plus_xy_A[1] and y_mouse <= rect_plus_xy_C[1]:
                if K<7:
                    K += 1
                else: pass
                # print ("Chuột nằm trong K+", x_mouse, y_mouse)

            # Tìm vị trí mouse K-
            if x_mouse >= rect_minus_xy_A[0] and x_mouse <= rect_minus_xy_B[0] and y_mouse >= rect_minus_xy_A[1] and y_mouse <= rect_minus_xy_C[1]:
                if K>0:
                    K -= 1
                else: pass
                # print ("Chuột nằm trong K-", x_mouse, y_mouse)

            # Tìm vị trí mouse Run
            if x_mouse >= rect_run_xy_A[0] and x_mouse <= rect_run_xy_B[0] and y_mouse >= rect_run_xy_A[1] and y_mouse <= rect_run_xy_C[1]:
                labels = []
                # Tìm khoảng cách min giữa các điểm points và clusters
                # Assgin points closet cluster                
                for point in points:
                    distance_points_clus = []
                    for clus in clusters:
                        disPoint_clus = fun_distance(point, clus)
                        distance_points_clus.append(disPoint_clus)
                    
                    # Tính khoảng cách gần nhất giữa 1 point với các clus 
                    min_distance = min(distance_points_clus)

                    # Tìm vị trí min_distance trong distance_points_clus, chính là vị trí trong Colors ===> this result assign for label
                    label = distance_points_clus.index(min_distance)                                      
                    " points dc gán cho label với giá trị = colors[i]"
                    labels.append(label)

                    # Update clusters: di chuyển cluster vào trung tâm từ k/c trung bình

                # new_clusters = []

                for k in range(K):
                    sum_x = 0
                    sum_y = 0
                    sum_point = 0

                    for i_point, point in enumerate(points):

                        # Số phần tử label= số phần tử points
                        " label là danh sách ghi lại màu của points"
                        if labels[i_point] == k: 
                            sum_x += point[0]
                            sum_y += point[1]
                            sum_point +=1

                    # Thay thế tọa độ mới cho cluster
                    if sum_point !=0:
                        clusters[k]= [sum_x/sum_point, sum_y/sum_point]
                 

            # Tìm vị trí mouse random
            if x_mouse >= rect_random_xy_A[0] and x_mouse <= rect_random_xy_B[0] and y_mouse >= rect_random_xy_A[1] and y_mouse <= rect_random_xy_C[1]:
                # clusters = [], để mỗi lần nhấn nút random thì xóa dữ liệu trước đó
                clusters=[]
                # Vẽ dg tròn random
                for k in range(K):
                    cluster = [randint(0, 700), randint(0, 500)]
                    clusters.append(cluster)
                
                # print ("Chuột nằm trong random", x_mouse, y_mouse)

            # Tìm vị trí mouse Algorithm
            if x_mouse >= rect_Algorithm_xy_A[0] and x_mouse <= rect_Algorithm_xy_B[0] and y_mouse >= rect_Algorithm_xy_A[1] and y_mouse <= rect_Algorithm_xy_C[1]:
                
                print ("Chuột nằm trong Algorithm", x_mouse, y_mouse)
            
            # Tìm vị trí mouse Reset
            if x_mouse >= rect_Reset_xy_A[0] and x_mouse <= rect_Reset_xy_B[0] and y_mouse >= rect_Reset_xy_A[1] and y_mouse <= rect_Reset_xy_C[1]:
                
                print ("Chuột nằm trong Reset", x_mouse, y_mouse)
                
    # Vẽ dg tròn random theo số lượng K
    for i_clus, cluster in enumerate(clusters):
        cen =(cluster[0] + 50, cluster[1] + 50)        
        # pygame.draw.circle(screen, black, center, 6)
        pygame.draw.circle(screen, colors[i_clus], cen, 20)
    
    # Vẽ đường tròn, dấu chấm theo tọa độ point
    for p in points:
        center =(p[0] + 50, p[1] + 50)        
        pygame.draw.circle(screen, black, center, 6)
        
        
        if labels ==[]:
            pygame.draw.circle(screen, white, center, 5)
        # gán và thay màu point cho điểm gần cluster nhất sau kh chạy nút run
        else:
            
            id_point = points.index(p) # Tìm vị trí có giá trị p trong points
            id_label = labels[id_point] # Tìm vị trí có giá trị id_point trong labels
            pygame.draw.circle(screen, colors[id_label], center, 5)


    pygame.display.flip() # cập nhật lại toàn bộ màn hình, thấy rõ khi vẽ vật thể di chuyển 
    #display.update () cho phép cập nhật một phần màn hình, thay vì toàn bộ khu vực màn hình
pygame.quit()