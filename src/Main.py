import pygame

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
                        elif self.menu == "game":
                            self.menu = "main"
                    elif event.key == pygame.K_SPACE:
                        if self.menu == "main":
                            self.menu = "game"

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

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
                    pass
                case "game":


                    self.drawBoard()

            pygame.display.flip()
            self.clock.tick(60)

    def drawBoard(self):
        pass


if __name__ == "__main__":
    main()
