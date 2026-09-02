import pygame

import Muehle
import Button

class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.windowWidth = 1500
        self.windowHeight = 1500

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.GL_DOUBLEBUFFER | pygame.RESIZABLE)
        pygame.display.set_caption("Muehle by David Derflinger")

        self.clock = pygame.time.Clock()
        self.running = True

        self.menu = "main"

        self.muehle = Muehle.Muehle()

        self.mainButtons = [Button.Button(self.screen, 150, 250, 1200, 200, (125, 90, 51), "1 Player"),
                            Button.Button(self.screen, 150, 600, 1200, 200, (125, 90, 51), "2 Player"),
                            Button.Button(self.screen, 150, 950, 1200, 200, (125, 90, 51), "Quit")]
        self.botButtons = []
        self.playerButtons = []


        self.backgroundColor = (133, 101, 66)
        self.headingColor = (82, 55, 26)
        self.baseColor = (102, 69, 32)

        self.run()

    def run(self):
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        if self.menu == "main":
                            self.running = False
                        elif self.menu in ["1player", "2player"]:
                            self.menu = "main"
                    elif event.key == pygame.K_SPACE:
                        if self.menu == "main":
                            self.muehle.reset()
                            self.menu = "1player"

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill(self.backgroundColor)

            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])

            oldMousePressed = mousePressed

            match self.menu:
                case "main":
                    font = pygame.font.Font(pygame.font.get_default_font(), 100)
                    text = font.render("Mühle", True, self.headingColor)
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth/2
                    newRect.centery = 100
                    self.screen.blit(text, newRect)

                    for button in self.mainButtons:
                        button.draw(textColor=self.headingColor)

                        if button.clicked(mx, my, mousePressedUp):
                            match button.onClick:
                                case "1 Player":
                                    self.muehle.reset()
                                    self.menu = "1player"
                                case "2 Player":
                                    self.muehle.reset()
                                    self.menu = "2player"
                                case "Quit":
                                    self.running = False
                case "1player":
                    font = pygame.font.Font(pygame.font.get_default_font(), 70)
                    text = font.render("1 Player", True, self.headingColor)
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.centery = 70
                    self.screen.blit(text, newRect)

                    self.drawBoard(200, 150, 1100, 1100)
                case "2player":
                    font = pygame.font.Font(pygame.font.get_default_font(), 70)
                    text = font.render("2 Player", True, self.headingColor)
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.centery = 70
                    self.screen.blit(text, newRect)

                    self.drawBoard(200, 150, 1100, 1100)

            pygame.display.flip()
            self.clock.tick(60)

    def drawBoard(self, posX, posY, sizeX, sizeY):
        lenX = len(self.muehle.board[0])
        lenY = len(self.muehle.board)

        for y in range(len(self.muehle.board)):
            for x in range(len(self.muehle.board[y])):
                color = self.baseColor

                oneX = int(sizeX/lenX)
                oneY = int(sizeY/lenY)

                curX = posX + x * oneX
                curY = posY + y * oneY

                thickness = int(oneX/4)

                match self.muehle.board[y][x]:
                    case "o":
                        pygame.draw.circle(self.screen, color, (curX+(oneX/2), curY+(oneY/2)), oneX/2)
                    case "-":
                        pygame.draw.rect(self.screen, color, (curX-1, curY+(oneY/2)-(thickness/2), oneX+2, thickness))
                    case "|":
                        pygame.draw.rect(self.screen, color, (curX+(oneX/2)-(thickness/2), curY-1, thickness, oneY+2))

        for y in range(len(self.muehle.board)):
            for x in range(len(self.muehle.board[y])):
                oneX = int(sizeX/lenX)
                oneY = int(sizeY/lenY)

                curX = posX + x * oneX
                curY = posY + y * oneY

                match self.muehle.board[y][x]:
                    case "w":
                        color = (255, 255, 255)
                        pygame.draw.circle(self.screen, color, (curX+(oneX/2), curY+(oneY/2)), oneX/1.5)
                    case "b":
                        color = (10, 10, 10)
                        pygame.draw.circle(self.screen, color, (curX + (oneX/2), curY+(oneY/2)), oneX/1.5)


if __name__ == "__main__":
    main()
