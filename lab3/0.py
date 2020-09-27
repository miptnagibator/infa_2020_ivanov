import pygame

def DrawArc(surface, color, center, radius, startAngle, stopAngle, width=1):
    width -= 2
    for i in range(-2, 3):
        # (2pi rad) / (360 deg)
        deg2Rad = 0.01745329251
        rect = pygame.Rect(
            center[0] - radius + i,
            center[1] - radius,
            radius * 2,
            radius * 2
        )

        pygame.draw.arc(
            surface,
            color,
            rect,
            startAngle * deg2Rad,
            stopAngle * deg2Rad,
            width
        )