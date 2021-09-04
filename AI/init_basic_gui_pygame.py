import pygame 

# Khởi tạo 1 số modul cơ bản pygame
pygame.init() #print("dfkgfdgkdf:", pygame.init())

# Tạo khung giao diện với [screen_width, screen_height] là list vì khung kéo dài từ vị trí 0
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
# screen = pygame.display.set_mode([1200,700])

# Tiêu đề cho chương trình
pygame.display.set_caption ("K_means visualization ")# visualization: hình dung

"Các biến để chạy: while running = True "
running = True # tạo biến running = True, chạy suốt chương trình
clock = pygame.time.Clock()
backgruond = (214, 214, 214)
# Tạo vòng lặp chạy suốt running =True, khi muốn tắt thì phải 
black = (0, 0, 0)
while running:
    clock.tick(60) # chạy screen 60 lần/ 1s
    screen.fill(backgruond)
    pygame.draw.rect(screen, black, (50,50,700,500))
    # "Lọc qua các event để tương tác nút tắt chương trình"    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # event.QUIT: nút x (màu đỏ), thoát
            running = False
    
    # show all các giá trị trong while (ko có sẽ ko thấy gì)
    pygame.display.flip()
pygame.quit()