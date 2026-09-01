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

    def draw(self, textColor=(255, 255, 255)):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        text = font.render(self.onClick, True, textColor)
        newRect = text.get_rect()
        newRect.centerx = self.x + self.width/2
        newRect.centery = self.y + self.height/2
        self.screen.blit(text, newRect)

    def clicked(self, mx, my, mouseClick):
        return self.hover(mx, my) and mouseClick[0]

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

