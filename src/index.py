import pygame
from sprites.enemies import Enemies
from waves import Waves


def main():
    pygame.init()
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tower Defence")
    running = True

    route = [(50, 0), (50, 200), (400, 200),
            (400, 400), (800, 400), (800, 720)]
    enemy = Enemies(route[0])
    wave = Waves()
    path_line = [(x-enemy.width//2, y-enemy.height//2) for x, y in route]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))
        pygame.draw.lines(screen, (128, 128, 128), False, route, 20)

        wave.spawn_enemies(route[0])
        wave.update_enemies(screen, path_line)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
