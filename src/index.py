import pygame
from gamelogic.tower_defence import TowerDefence

def main():
    pygame.init()
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tower Defence")
    running = True

    td = TowerDefence()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))
        pygame.draw.lines(screen, (128, 128, 128), False, td.route, 20)

        td.spawn_enemies()
        td.update_enemies(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
