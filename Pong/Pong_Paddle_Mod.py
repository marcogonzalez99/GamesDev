import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y,player_score,opponent_score,score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball Border
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        
    #Collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0 + 5
    if player.bottom >= screen_height:
        player.bottom = screen_height - 5
    
def opponent_ai():
    if opponent.top < ball.y - 55: # This adjustment is for how strong the AI will be
        opponent.top += opponent_speed
    if opponent.bottom > ball.y + 55: # This adjustment is for how strong the AI will be
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0 + 5
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height - 5
            
def ball_restart():
    global ball_speed_x,ball_speed_y,score_time,player,opponent
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2 - 5, screen_height/2 - 5)
    
    if current_time - score_time < 2100:
        mod_message = game_font.render("Randomizing Paddles...", False, (255,255,255))
        screen.blit(mod_message, (200, 20))
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, (0,255,255))
        screen.blit(number_three, (355,50))
    if current_time - score_time < 1400 and current_time - score_time > 700:
        number_two = game_font.render("2", False, (0,255,255))
        screen.blit(number_two, (355,100))
        ballMod()
    if current_time - score_time < 2100 and current_time - score_time > 1400:
        number_one = game_font.render("1", False, (0,255,255))
        screen.blit(number_one, (355,150))
    
    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        speed = random.choice((5,10))
        ball_speed_y = speed * random.choice((1,-1))
        ball_speed_x = speed * random.choice((1,-1))
        score_time = None            
        
def score_logic():
    if (player_score >= 7):
        msg = game_font.render("Player Won", False, light_grey)
        screen.blit(msg,(290, 300))
        game_end()
    if (opponent_score >= 7):
        msg = game_font.render("CPU Won", False, light_grey)
        screen.blit(msg,(305, 300))
        msg2 = game_font.render("Game Over", False, light_grey)
        screen.blit(msg2,(290, 330))
        game_end()

def ballMod():
    global player,opponent
    player = pygame.Rect(screen_width - 20, screen_height/2 - 70,15,random.choice((50,150)))
    opponent = pygame.Rect(10, screen_height/2 - 70,15,random.choice((75,200)))

def game_end():
    global ball_speed_x,ball_speed_y
    ball_speed_x,ball_speed_y = 0,0
        
#General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong - Paddle Mod")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 10,screen_height/2 - 10,20,20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,15,100)
opponent = pygame.Rect(10, screen_height/2 - 70,15,100)

background = pygame.Color('grey12')
light_grey = (200,200,200)
player_color = (175,175,175)
opponent_color = (200,200,200)
ball_color = (255,255,255)

# Game Variabes
ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponent_speed = 7

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 24)

# Score Timer
score_time = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
                      
    ball_animation()
    player_animation()
    opponent_ai()
    
    #Visuals - In order from top to bottom
    screen.fill(background)        
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, opponent_color, opponent)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height)) 
    score_logic()
    
    if score_time:
        ball_restart()
          
    player_text = game_font.render(f"Player: {player_score}", False, light_grey)
    screen.blit(player_text,(470,240))   
    
    opponent_text = game_font.render(f"CPU: {opponent_score}", False, light_grey)
    screen.blit(opponent_text,(150,240))   
                 
    pygame.display.flip()
    clock.tick(60)
    