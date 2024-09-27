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

    # player.draw(surface)
    # for car in cars:
    #     car.draw(surface)


    draw_grid(surface)
    pygame.display.flip()



def update():
    player.update()
    for car in cars:
        car.update()





# ONLY CHANGE THIS CODE
def draw_grid(surface):
    #  surface, (color), (start_pos), (end_pos), line_width
    #pygame.draw.line(surface, (255, 255, 255), (0, 0), (GAME_WIDTH, GAME_HEIGHT), 5)
    for x in range(COLS + 1):
        vertical_line = x * (BLOCK_SIZE)
        pygame.draw.line(surface, (255, 255, 255), (vertical_line, 0), (vertical_line, GAME_HEIGHT), 5)


    for y in range(ROWS):
        horizontal_line = y * (BLOCK_SIZE)
        pygame.draw.line(surface, (255, 255, 255), (0, horizontal_line), (GAME_WIDTH, horizontal_line), 5)

        # surface, (color), rect(x, y, width, height), ?Line widith no fill
    pygame.draw.rect(surface, (255, 255, 255), (0, 0, GAME_WIDTH, GAME_HEIGHT), 5)
    pygame.draw.rect(surface, (255, 0, 255), (0, 0, BLOCK_SIZE, BLOCK_SIZE))





#######################################

if __name__ == "__main__":
    main()
