import pygame
import pygame_gui
import sys as sus
import consts

class MainMenu:
    def __init__(self):
        self.manager = pygame_gui.UIManager((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

        center_x = consts.SCREEN_WIDTH // 2
        start_y = 100
        spacing = 70
        button_width, button_height = 200, 50

        # Заголовок по центру
        self.title_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((center_x - 200, 30), (400, 70)),
            text='SPACE ACROPOLIS',
            manager=self.manager
        )

        # Кнопки ровно по центру
        self.play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((center_x - button_width // 2, start_y), (button_width, button_height)),
            text='Играть',
            manager=self.manager
        )

        self.upgrade_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((center_x - button_width // 2, start_y + spacing), (button_width, button_height)),
            text='Улучшения',
            manager=self.manager
        )

        self.settings_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((center_x - button_width // 2, start_y + spacing * 2), (button_width, button_height)),
            text='Настройки',
            manager=self.manager
        )

        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((center_x - button_width // 2, start_y + spacing * 3), (button_width, button_height)),
            text='Выход из игры',
            manager=self.manager
        )

        self.pause = True

    def update_in_cycle(self, event, respawn):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.play_button:
                print("Начинаем игру!")
                self.pause = False
                respawn()
            elif event.ui_element == self.upgrade_button:
                print("Открываем улучшения.")
            elif event.ui_element == self.settings_button:
                print("Настройки открыты.")
            elif event.ui_element == self.quit_button:
                print("Выход из игры.")
                pygame.quit()
                sus.exit()

        self.manager.process_events(event)

    def update(self, clock):
        time_delta = clock.tick(60) / 1000.0
        self.manager.update(time_delta)

    def draw(self, screen):
        self.manager.draw_ui(screen)


