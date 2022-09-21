import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y,ball2_speed_x,ball2_speed_y,player_score,opponent_score,score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    ball2.x += ball2_speed_x
    ball2.y += ball2_speed_y
    
    # Ball Border
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        ball_restart()
        
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()
        
    # Ball 2 Border
    if ball2.top <= 0 or ball2.bottom >= screen_height:
        ball2_speed_y *= -1
    if ball2.left <= 0:
        player_score += 1
        ball2_restart()
        
    if ball2.right >= screen_width:
        opponent_score += 1
        ball2_restart()
    
    #Collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    if ball2.colliderect(player) or ball2.colliderect(opponent):
        ball2_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0 + 5
    if player.bottom >= screen_height:
        player.bottom = screen_height - 5
    
def opponent_ai():
    if ball.x <360 or ball.x < ball2.x:
        if opponent.top < ball.y - 40: # This adjustment is for how strong the AI will be
            opponent.top += opponent_speed
        if opponent.bottom > ball.y + 40: # This adjustment is for how strong the AI will be
            opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0 + 5
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height - 5
    if ball2.x <360 or ball2.x < ball.x:
        if opponent.top < ball2.y - 40: # This adjustment is for how strong the AI will be
            opponent.top += opponent_speed # Moves the Ai up the set "speed"
        if opponent.bottom > ball2.y + 40: # This adjustment is for how strong the AI will be
            opponent.bottom -= opponent_speed # Moves the Ai down the set "Speed"
        if opponent.top <= 0: #Prevents the Ai from going off the screen
            opponent.top = 0 + 5 # Saves 5 pixels from the top for the Ai to not go beyond
        if opponent.bottom >= screen_height: # Prevents the Ai from going off the screen
            opponent.bottom = screen_height - 5 # Saves 5 pixels from the bottom for the Ai to not go past
    if ball2.x == ball.x and ball2.x <360: #Priority System to prevent the Ai from conceeding two goals at the same time, targets the second ball
        if opponent.top < ball2.y - 40: # This adjustment is for how strong the AI will be
            opponent.top += opponent_speed
        if opponent.bottom > ball2.y + 40: # This adjustment is for how strong the AI will be
            opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0 + 5
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height - 5
            
def ball_restart():
    global ball_speed_x,ball_speed_y
    
    ball.center = (screen_width/2, screen_height/2)
    
    speed = 8
    ball_speed_y = speed * random.choice((1,-1))
    ball_speed_x = speed * random.choice((1,-1))
        
               
def ball2_restart():
    global ball2_speed_x,ball2_speed_y
    ball2.center = (screen_width/2, screen_height/2)
    
    speed = 8
    ball2_speed_y = speed * random.choice((1,-1))
    ball2_speed_x = speed * random.choice((1,-1))
    

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

def game_end():
    global ball_speed_x,ball_speed_y,ball2_speed_x,ball2_speed_y
    ball_speed_x,ball_speed_y = 0,0
    ball2_speed_x,ball2_speed_y = 0,0
        
#General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong - Double Ball Mod")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 10,screen_height/2 - 10,20,20)
ball2 = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20,20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,15,100)
opponent = pygame.Rect(10, screen_height/2 - 70,15,100)

background = pygame.Color('grey12')
light_grey = (200,200,200)
player_color = (175,175,175)
opponent_color = (200,200,200)
ball_color = (255,255,255)
ball2_color = (15,150,150)

# Game Variabes
ball_speed_x = 8 * random.choice((-1,1)) 
ball_speed_y = 8 * random.choice((-1,1)) 

ball2_speed_x = 8 * random.choice((-1,1))
ball2_speed_y = 8 * random.choice((-1,1)) 

player_speed = 0
opponent_speed = 8

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 24)


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
    pygame.draw.ellipse(screen, ball2_color, ball2) 
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height)) 
    score_logic()
          
    player_text = game_font.render(f"Player: {player_score}", False, light_grey)
    screen.blit(player_text,(465,240))   
    
    opponent_text = game_font.render(f"CPU: {opponent_score}", False, light_grey)
    screen.blit(opponent_text,(150,240))   
    
    if ball2_speed_x == ball_speed_x and ball2_speed_y == ball_speed_y and ball.x == ball2.x and ball.y == ball2.y and ball2_speed_x != 0 and ball_speed_x !=0:
        double_point = game_font.render("Double Points", False, (255,255,255))
        screen.blit(double_point, (275,30))
                 
    pygame.display.flip()
    clock.tick(60)
    