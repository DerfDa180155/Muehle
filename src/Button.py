import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color, onClick):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.onClick = onClick

        self.isHovered = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def clicked(self, mx, my, mouseClick):
        return self.hover(mx, my) and mouseClick[0]

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

