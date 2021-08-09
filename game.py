import pygame 
import random 
import time 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# play music
game_sound = pygame.mixer.Sound('retro-run.wav')
game_sound.play(-1)


# Create the player, enemy, prize objects and give them appropriate pictures

background = pygame.image.load("background.jpg")
player = pygame.image.load("player.png")
enemy1 = pygame.image.load("monster1.png")
enemy2 = pygame.image.load("monster2.png")
enemy3 = pygame.image.load("monster3.png")
fire1 = pygame.image.load("fire.png")
fire2 = pygame.image.load("fire.png")
fire3 = pygame.image.load("fire.png")
prize  = pygame.image.load("prize.png")
win    = pygame.image.load("win.png")
lose   = pygame.image.load("lose.png")
losef   = pygame.image.load("losef.png")

# Get the width and height of the images in order to do boundary detection 

player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
fire1_height = fire1.get_height()
fire1_width = fire1.get_width()
fire2_height = fire2.get_height()
fire2_width = fire2.get_width()
fire3_height = fire3.get_height()
fire3_width = fire3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Store the positions of the player, enemy and prize as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.
# Make some enemies start from further out so they dont spawn on top of each other

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  screen_width + 550
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width + 1200
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
fire1XPosition =  screen_width + 300
fire1YPosition =  random.randint(0, screen_height - fire1_height)
fire2XPosition =  screen_width + 750
fire2YPosition =  random.randint(0, screen_height - fire2_height)
fire3XPosition =  screen_width + 1000
fire3YPosition =  random.randint(0, screen_height - fire3_height)

prizeXPosition = screen_width - prize_width 
prizeYPosition = screen_height - prize_height 

backgroundXPosition = screen_width - screen_width
backgroundYPosition = screen_height - screen_height

winXPosition = screen_width-1040
winYPosition = screen_height-680
loseXPosition = screen_width-screen_width
loseYPosition = screen_height-screen_height
losefXPosition = screen_width-1040
losefYPosition = screen_height-680

# check if the up or down key is pressed. Starts at False (not pressed). True when pressed

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# Game loop

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). 

    screen.fill(0) # Clears the screen.
    screen.blit(background, (backgroundXPosition, backgroundYPosition))
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the position specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(fire1, (fire1XPosition, fire1YPosition))
    screen.blit(fire2, (fire2XPosition, fire2YPosition))
    screen.blit(fire3, (fire3XPosition, fire3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

            

    # check key pressed values and move player accordingly.
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
        
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1    
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player beyond the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:# This makes sure that the user does not move the player before the window.
            playerXPosition += 1
            
    
    # Check for collision of the enemy with the player by building bounding boxes around their images
    # Test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    fire1Box = pygame.Rect(fire1.get_rect())
    fire1Box.top = fire1YPosition
    fire1Box.left = fire1XPosition

    fire2Box = pygame.Rect(fire2.get_rect())
    fire2Box.top = fire2YPosition
    fire2Box.left = fire2XPosition

    fire3Box = pygame.Rect(fire3.get_rect())
    fire3Box.top = fire3YPosition
    fire3Box.left = fire3XPosition

    # Bounding box for prize

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
        game_sound.stop()
        lose_sound = pygame.mixer.Sound('lose.wav')
        lose_sound.play()
        screen.blit(lose, (loseXPosition, loseYPosition))
        pygame.display.flip()

        # pause screen 
        time.sleep(8)

        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(fire1Box) or playerBox.colliderect(fire2Box) or playerBox.colliderect(fire3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
        game_sound.stop()
        lose_sound = pygame.mixer.Sound('lose.wav')
        lose_sound.play()
        screen.blit(losef, (losefXPosition, losefYPosition))
        pygame.display.flip()

        # pause screen 
        time.sleep(8)

        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    # If the enemy is off the screen the user wins the game:
    
    if enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width:
    
        # Display winning status to the user: 
        
        print("You win!")
        game_sound.stop()
        win_sound = pygame.mixer.Sound('win.wav')
        win_sound.play()

        screen.blit(win, (winXPosition, winYPosition))
        pygame.display.flip()

        # pause screen 
        time.sleep(8)

        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

    # If the player collides with (gets) the prize

    if playerBox.colliderect(prizeBox):
        print("You win!")
        game_sound.stop()
        prize_sound = pygame.mixer.Sound('retro-casino.wav')
        prize_sound.play()
        win_sound = pygame.mixer.Sound('win.wav')
        win_sound.play()

        screen.blit(win, (winXPosition, winYPosition))
        pygame.display.flip()
        
        # pause screen 
        time.sleep(8)
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
 
    
    # Make enemy approach the player.
    
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15
    fire1XPosition -= 0.15
    fire2XPosition -= 0.15
    fire3XPosition -= 0.15
