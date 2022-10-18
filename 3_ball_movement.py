import pygame
import os


# 기본 초기화 (반드시 해야하는 것들)
#################################################################################

pygame.init() # 초기화(반드시 필요!)

# 화면 크기 설정하기
screen_width = 640 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("PANG") #게임이름

# FPS
clock = pygame.time.Clock()

#################################################################################



#################################################################################
# 1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "image") #image폴더 위치 반환

#배경만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))
#반환한 os로 절대경로 없이 파일 불러오기

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위함

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = screen_height - character_height - stage_height


#캐릭터(스프라이트) 불러오기

# 이동할 좌표 변수
# 이동속도
character_to_x = 0
character_speed = 5

# 무기만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해서 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]


# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] #공 0123의 속도

#공들 #딕셔너리
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, #공의 x좌표
    "pos_y" : 50, #공의 y좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x":3, #x축 이동방향, -3이면 왼쪽, 3이면 오른쪽
    "to_y": -6,
    "init_spd_y" : ball_speed_y[0]}) # 최초속도



# 적 enemy 캐릭터


# 폰트 정의


# 총 시간


# 시간계산
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아뒀다가 나중에 빼는 방식. 파이썬 대표적인 방식


#################################################################################

# 창이 꺼지지 않게 이벤트 루프
running = True #게임이 실행중인가요?
while running :
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정함 #높을수록 부드러움


# 2. 이벤트 처리하기(키보드, 마우스 등)

    for event in pygame.event.get() :
        #파이게임을 쓰기 위해서는 무조건 적어야함. 키보드 입력이나 마우스 입력이 있는지 체크하는 코드
        if event.type == pygame.QUIT : #창이 닫히는 이벤트가 발생했나요?
            running = False # 게임 진행중이 아니네요

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT : 
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE :
                weapon_x_pos = character_x_pos + (character_width /2) - (weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0
        

# 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

# 무기 위치 조정하기
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기위치를 위로! y값이 스피드만큼 빠지는
    # 100, 200 -> 180, 160 ......

#천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

# 공 위치 정의
    for ball_idx, ball_val in enumerate(balls) : #공의 인덱스 정보가 필요
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

# 공 튕기기
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width :
            ball_val["to_x"] = ball_val["to_x"] * -1
        
        if ball_pos_y >= screen_height - stage_height - ball_height :
            ball_val["to_y"] = ball_val["init_spd_y"] #스테이지에 닿으면 튕기는 처리
        else : 
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


 
  
# 4. 충돌처리
    # 충돌처리를 위한 rect정보 업데이트 -> 적에 닿으면 쾅 하고 게임 꺼지기
 
    # 충돌체크 #colliderect ->충돌했는지 확인하는 함수
   

    
# 5. 화면에 그리기
    screen.blit(background,(0,0)) # 배경 그리기 # 0,0위치는 좌측 최상단 기준

   #무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    for idx, val in enumerate(balls) :
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))


    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))

 



  
    pygame. display.update() # 게임화면에 배경 등이 그려진 채로 유지하기

# 6. 게임 종료하기

pygame.quit()
