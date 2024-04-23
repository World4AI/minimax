import pygame
from sys import exit
from minimax import Game

WIDTH = 500
HEIGHT = 500
MARGIN = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tic-tac-toe")
clock = pygame.time.Clock()
font = pygame.font.Font("font/OpenSans-VariableFont_wdth,wght.ttf", 60)
game = Game()

# variables for drawing on the screen
line_len = min(WIDTH, HEIGHT) - MARGIN * 2
gap = line_len / 3

while True:
    state = game.get_state()
    game_over = game.is_terminal(state)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                x, y = event.pos
                x = (x - MARGIN) / gap
                y = (y - MARGIN) / gap

                if x > 0 and x < 3 and y > 0 and y < 3:
                    row = int(y)
                    col = int(x)
                    game.make_move((row, col))
                    game.make_move()

    screen.fill("black")

    if game_over:
        utility = game.utility(state)
        if utility == 1:
            text = font.render("X Won", True, "white")
        elif utility == -1:
            text = font.render("O Won", True, "white")
        else:
            text = font.render("Draw", True, "white")

        text_rect = text.get_rect()
        text_rect.center = (
            int(WIDTH / 2),
            int(50),
        )
        screen.blit(text, text_rect)

    # draw lines
    pygame.draw.line(
        screen, "white", (MARGIN, MARGIN + gap), (MARGIN + line_len, MARGIN + gap)
    )
    pygame.draw.line(
        screen,
        "white",
        (MARGIN, MARGIN + gap * 2),
        (MARGIN + line_len, MARGIN + gap * 2),
    )

    pygame.draw.line(
        screen, "white", (MARGIN + gap, MARGIN), (MARGIN + gap, MARGIN + line_len)
    )

    pygame.draw.line(
        screen,
        "white",
        (MARGIN + gap * 2, MARGIN),
        (MARGIN + gap * 2, MARGIN + line_len),
    )

    # draw X and O
    for r, row in enumerate(state):
        for c, value in enumerate(row):
            if value is not None:
                text = font.render(value, True, "white")
                text_rect = text.get_rect()
                text_rect.center = (
                    int(MARGIN + c * gap + gap / 2),
                    int(MARGIN + r * gap + gap / 2),
                )
                screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)
