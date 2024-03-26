import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Screen setup
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey Clock")

# Load images
mickey_body = pygame.image.load("D:\Distr\System\Desktop\python")  # Update path to your image
minute_hand = pygame.image.load("D:\Distr\System\Desktop\python")  # Update path to your image
second_hand = pygame.image.load("D:\Distr\System\Desktop\python")  # Update path to your image

# Main clock loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get current time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    
    # Calculate rotation angles
    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360
    
    # Rotate hands
    rotated_minute_hand = pygame.transform.rotate(minute_hand, -minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, -second_angle)
    
    # Calculate offsets for rotated images
    minute_offset = rotated_minute_hand.get_rect(center=minute_hand.get_rect(topleft=(200, 200)).center)
    second_offset = rotated_second_hand.get_rect(center=second_hand.get_rect(topleft=(200, 200)).center)
    
    # Draw everything
    screen.fill((255, 255, 255))  # White background
    screen.blit(mickey_body, (0, 0))
    screen.blit(rotated_minute_hand, minute_offset.topleft)
    screen.blit(rotated_second_hand, second_offset.topleft)
    
    pygame.display.flip()
    clock.tick(60)
