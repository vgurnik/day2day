import pygame

def get_mouse(base_res, current_res):
    """Возвращает позицию мыши в координатах внутреннего разрешения"""
    mouse_pos = pygame.mouse.get_pos()
    return (round(mouse_pos[0] / current_res[0] * base_res[0]),
            round(mouse_pos[1] / current_res[1] * base_res[1]))


def render(display, screen, base_res, current_res):
    """Отрисовывает screen на display с учетом масштабирования, с черными полосками"""
    aspect = base_res[1] / base_res[0]
    if current_res[1] / current_res[0] == aspect:
        display.blit(pygame.transform.scale(screen, current_res), (0, 0))
    elif current_res[1] / current_res[0] > aspect:
        diff = round(current_res[1] - current_res[0] * aspect)
        display.blit(pygame.transform.scale(screen, (current_res[0], current_res[1] - diff)),
                          (0, diff // 2))
    else:
        diff = round(current_res[0] - current_res[1] / aspect)
        display.blit(pygame.transform.scale(screen, (current_res[0] - diff, current_res[1])),
                          (diff // 2, 0))
