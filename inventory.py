from pytmx import load_pygame

from settings import *

class inventory:
    def __init__(self, logs, seeds):

        self.clicked = False

        self.n_logs = logs
        self.n_seeds = seeds

        self.icon_size = (50, 50)
        self.n_overlays = 2
        self.overlay_distance = WINDOW_HEIGHT / (self.n_overlays + 1)
        self.right_margin = WINDOW_WIDTH - (WINDOW_WIDTH / 10)

        self.log_image = pygame.image.load(os.path.join('data','Graphics','icons','log.png')).convert()
        self.log_image = pygame.transform.scale(self.log_image, self.icon_size)
        self.log_image.set_colorkey((128, 128, 128))
        self.log_rect = pygame.Rect(self.right_margin, self.overlay_distance, self.log_image.width, self.log_image.height)

        self.seed_image = pygame.image.load(os.path.join('data','Graphics','icons','seeds1.png')).convert_alpha()
        self.seed_image = pygame.transform.scale(self.seed_image, self.icon_size)
        self.seed_rect = pygame.Rect(self.right_margin, self.overlay_distance * 2, self.seed_image.width, self.seed_image.height)

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 40)
        self.font_color = (255, 255, 255)

        self.log_text = ""
        self.seed_text = ""
        self.log_text_pos = (self.log_rect.x + self.log_rect.width/4, self.log_rect.y + 50)
        self.seed_text_pos = (self.seed_rect.x + self.seed_rect.width/4, self.seed_rect.y + 50)

    def update(self):
        self.log_text = self.font.render(str(self.n_logs), True, self.font_color)
        self.seed_text = self.font.render(str(self.n_seeds), True, self.font_color)

    def check_collect(self, trees, offset):
        if pygame.mouse.get_pressed()[0]:
            if not self.clicked:
                mx, my = pygame.mouse.get_pos()

                world_mouse = (mx - offset.x, my - offset.y)

                for sprite in trees:
                    # print(sprite.rect.x, sprite.rect.y)
                    if sprite.rect.collidepoint(world_mouse):
                        # print("Clicked tree!!")
                        self.n_logs += 1
                        break

                # print(f"World mouse: {world_mouse}")
                self.clicked = True
        else:
            self.clicked = False


    def draw_all(self, screen, trees, offset):
        self.check_collect(trees, offset)
        self.update()
        screen.blit(self.log_image, self.log_rect)
        screen.blit(self.seed_image, self.seed_rect)
        screen.blit(self.log_text, self.log_text_pos)
        screen.blit(self.seed_text, self.seed_text_pos)