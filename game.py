import pygame

import config
from alien import Alien
from bullet import Bullet
from player import Player

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

game_running = True

player = Player(screen)

bullets = []
aliens = []

level = 0

while game_running:
    drop_aliens = False
    clock.tick(24)
    screen.fill((0,0,0))

    # level check
    if len(aliens) <= 0:
        level = level + 1
        line = 1
        x_position = 0

        for x in range(config.NUMBER_OF_ALIENS):
            if x_position * config.SCALE * 2 + 100 > config.SCREEN_WIDTH:
                line = line + 1
                x_position = 0

            alien = Alien(screen, x_position * config.SCALE * 2, line * config.SCALE, level)
            x_position = x_position + 1
            aliens.append(alien)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            if event.key == pygame.K_LEFT:
                player.position = player.position - config.SCALE
            if event.key == pygame.K_RIGHT:
                player.position = player.position + config.SCALE
            if event.key == pygame.K_SPACE:
                bullet = Bullet(screen, player.position, config.SCREEN_HEIGHT - config.SCALE, -10)
                bullets.append(bullet)

    for bullet in bullets:
        for alien in aliens:
            if alien.collide(bullet.position[0], bullet.position[1]):
                alien.killed = True
                bullet.killed = True

        bullet.update()
        bullet.render()

    for alien in aliens:
        if alien.killed:
            aliens.remove(alien)
            continue

        alien.update()
        alien.render()

        if alien.position[0] >= (config.SCREEN_WIDTH - 5) or alien.position[0] < 0:
            drop_aliens = True

    if drop_aliens:
        for alien in aliens:
            alien.drop()

    for bullet in bullets:
        if bullet.killed:
            bullets.remove(bullet)

    player.render()

    pygame.display.flip()