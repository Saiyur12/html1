import pythongame

# Initialize Pygame and screen dimensions
pythongame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title
display_surface = pythongame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pythongame.display.set_caption('Adding image and background image')

# Load and scale images directly
background_image = pythongame.transform.scale(
    pythongame.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pythongame.transform.scale(
    pythongame.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2 - 30))

# Initialize font, render text, and set text position
text = pythongame.font.Font(None, 36).render('Hello World ', True,
                                             pythongame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pythongame.time.Clock()
    running = True
    while running:
        for event in pythongame.event.get():
            if event.type == pythongame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pythongame.display.flip()
        clock.tick(30)

    pythongame.quit()


if __name__ == '__main__':
    game_loop()