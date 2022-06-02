import pygame
from random import *

#'이미지 불러오기'의 이미지 주소 값은 제 노트북을 기준으로 임의로 설정된 것들입니다.

#초기화
pygame.init()

#화면 타이틀 설정 (게임 이름)
pygame.display.set_caption("KUCC")

#FPS
clock =pygame.time.Clock()

#시작 시간
start_ticks = pygame.time.get_ticks()

#배경 이미지 불러오기
background = pygame.image.load("images/background.png")
background_size = background.get_rect().size #이미지 크기
background_width = background_size[0]
background_height = background_size[1]
screen_width = background_size[0]
screen_height = background_size[1]
screen = pygame.display.set_mode((screen_width, screen_height))
pad_width=background_width
pad_height=background_height
background1=background.copy()
background2=background1.copy()

x = pad_width * 0.5
y = pad_height * 0.8
y_change = 0

background1_x = 0
background2_x = background_width

WHITE=(255,255,255)
gamepad = pygame.display.set_mode((pad_width, pad_height))


def back(background,x,y):
    global gamepad
    gamepad.blit(background,(x,y))


#캐릭터(스프라이트) 불러오기
character = pygame.image.load("images/plane.png")
character_size = character.get_rect().size #이미지 크기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 100
character_y_pos = 100

#장애물 캐릭터
enemy = pygame.image.load("images/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos =  randrange(0,1024)
enemy_y_pos = 0

#이동할 좌표
to_y = 0
#이동속도
character_speed = 0.4
enemy_speed = 0.5

#폰트 정의
game_font = pygame.font.Font(None, 60)

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수



    for event in pygame.event.get():
        #게임 종료
        if event.type == pygame.QUIT: running = False
        #캐릭터 조작
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: to_y -= character_speed
            elif event.key == pygame.K_DOWN: to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: to_y = 0
    character_y_pos += to_y * dt

    ##배경 이동
    y += y_change
    gamepad.fill(WHITE)

    background1_x -= 2
    background2_x -= 2

    if background1_x == -background_width:
        background1_x = background_width

    if background2_x == -background_width:
        background2_x = background_width

    back(background1, background1_x, 0)
    back(background2, background2_x, 0)

    #세로 경계값 처리
    if character_y_pos < 0: character_y_pos = 0
    elif character_y_pos > background_height - character_height:character_y_pos = background_height - character_height


    #장애물 동작
    enemy_x_pos -= enemy_speed * dt
    if enemy_x_pos < 0:
        enemy_x_pos = 740
        enemy_y_pos =  randrange(0,370 - enemy_height)

    #충돌 처리를 위한 react 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #이미지 그리기
    gamepad.blit(character,(character_x_pos,character_y_pos))
    gamepad.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #충돌처리
    end = game_font.render("Game Over", True, (0,0,0))
    if character_rect.colliderect(enemy_rect):
        gamepad.blit(end, (250,150))
        running = False

    #점수 출력
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/ 1000
    score = game_font.render(str(int(elapsed_time)*10), True, (225,225,225))
    screen.blit(score, (10,10))


    #게임화면 다시 그리기
    pygame.display.update()

#잠시 대기
pygame.time.delay(500)
#pygame 종료
pygame.quit()