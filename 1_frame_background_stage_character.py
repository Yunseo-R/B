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


        

# 3. 게임 캐릭터 위치 정의

  
# 4. 충돌처리
    # 충돌처리를 위한 rect정보 업데이트 -> 적에 닿으면 쾅 하고 게임 꺼지기
 
    # 충돌체크 #colliderect ->충돌했는지 확인하는 함수
   

    
# 5. 화면에 그리기
    screen.blit(background,(0,0)) # 배경 그리기 # 0,0위치는 좌측 최상단 기준
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))


  
    pygame. display.update() # 게임화면에 배경 등이 그려진 채로 유지하기

# 6. 게임 종료하기

pygame.quit()
