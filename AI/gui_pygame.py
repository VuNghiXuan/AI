
import pygame
from Package.fun_Gui import fun_poss_three_rectangular_points

pygame.init()

wight_group = 1200
heigh_group = 700
screen = pygame.display.set_mode([wight_group, heigh_group])

running = True
clock = pygame.time.Clock()

background = (214, 214, 214)

# vẽ khung hcn chương trình đè lên BACKGROUP
black = (0, 0, 0) # Đường viền đen
background_panel = (250, 255, 230) # màu panel 
white = (255, 255, 255)
# three_hCN = fun_poss_three_rectangular_points((50,50), 700,500)
font = pygame.font.SysFont('sans', 40)
text_plus = font.render('+', True, white) # render: hiển thị (bề mặt)

#  HCN_text plus (850, 50, 50, 50))
rect_plus_xy_A,  rect_plus_xy_B, rect_plus_xy_C, rect_plus_xy_D = fun_poss_three_rectangular_points((850,50), 50,50)

while running:
    clock.tick(60) 
    screen.fill(background)

    # Vẽ interface
    pygame.draw.rect(screen, black, (50,50,700,500))

    # Draw panel
    pygame.draw.rect(screen, background_panel, (55, 55, 690, 490))

    # Draw hcn text_plus
    pygame.draw.rect(screen, black, (850, 50, 50, 50))
    screen.blit(text_plus, (865, 50)) # phương thức blit: Vẽ nhiều bề mặt lên Bề mặt này

    # Tìm vị trí mouse
    x_mouse, y_mouse = pygame.mouse.get_pos()
    if x_mouse >= rect_plus_xy_A[0] and x_mouse <= rect_plus_xy_B[0] and y_mouse >= rect_plus_xy_A[1] and y_mouse <= rect_plus_xy_C[1]:
        print ("Chuột nằm trong", x_mouse, y_mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip() # cập nhật lại toàn bộ màn hình, thấy rõ khi vẽ vật thể di chuyển 
    #display.update () cho phép cập nhật một phần màn hình, thay vì toàn bộ khu vực màn hình
pygame.quit()