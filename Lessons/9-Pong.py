# Lesson 3
import pygame
import sys
import random
    
#General Setup
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 2, 512)

#Screen Sizes
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(("Pong - Lesson 6"))

#Game Rectanbgles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2-15,30,30) #This places the ball in the middle of the screen
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 120) #This will place the Player Paddle on the right side of the screen
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 120) #This will place the Opponent Paddle on the the left side of the screen

#Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

# Game Variables
ball_speed_x = 12
ball_speed_y = 12
player_speed = 0
opponent_speed = 8

# Score Varaibles
player_score = 0
opponent_score = 0
game_font = pygame.font.Font(None,44)

# Game Sounds
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("wall.ogg")


def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y 
    
    # Ball Collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        
    if ball.left <= 0:
        player_score += 1
        score_sound.play()
        ball_restart()
    if ball.right >= screen_width:
        opponent_score += 1
        score_sound.play()
        ball_restart()
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        pong_sound.play()
        ball_speed_x *= -1   

def player_animation():
    player.y += player_speed
    #Player Collision
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height    
    
def opponent_ai():
    if opponent.top < ball.y:  # This adjustment is for how strong the AI will be
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:  # This adjustment is for how strong the AI will be
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0 + 5
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height - 5
        
def ball_restart():
    global ball_speed_x,ball_speed_y
    ball_speed_x *= random.choice((-1,1))
    ball_speed_y *= random.choice((-1,1))
    ball.center = (screen_width/2, screen_height/2)
    
if __name__ == "__main__":
    # Game Loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 12
                if event.key == pygame.K_UP:
                    player_speed -= 12
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 12
                if event.key == pygame.K_UP:
                    player_speed += 12
                    
        ball_animation()
        player_animation()
        opponent_ai()
        
        screen.fill(bg_color)        
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
        
        # Surface for scoreboard
        player_test = game_font.render(f"{opponent_score} : {player_score}",False,('white'))
        screen.blit(player_test,(screen_width/2 - 30,screen_height/2))
        
        pygame.display.flip()
        clock.tick(60)  