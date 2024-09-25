from constants import *
import pygame
import player
import car

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

player = player.Player()
cars = []
for i in range(5):
    cars.append(car.Car())


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_LEFT:
                    player.move_left()


        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background

    player.draw(surface)
    for car in cars:
        car.draw(surface)
    pygame.display.flip()



def update():
    player.update()
    for car in cars:
        car.update()

if __name__ == "__main__":
    main()
