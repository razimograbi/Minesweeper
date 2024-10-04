import pygame

def RenderScreen(background_color: tuple, screen: pygame.Surface, camera_group: pygame.sprite.Group,
                 delay_time_in_millie=0):
    screen.fill(background_color)
    camera_group.update()
    camera_group.draw(screen)
    pygame.display.update()
    if delay_time_in_millie > 0:
        pygame.time.delay(delay_time_in_millie)
