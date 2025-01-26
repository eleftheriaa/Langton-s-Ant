import pygame,sys
pygame.init()
directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

class Mainarw():
    def __init__(self,size,rows,window):
        self.size=size
        self.rows=rows
        self.window=window
        self.create()
    def create(self):
        dis = self.size // self.rows
        self.window.fill((0,0,0))
        font = pygame.font.Font(None, 30)
        text = font.render("  langton's ant  ", True,(0,0,0),(215,215,215))
        for x in range(self.size):
            for y in range(self.rows):
                if (x==200 and y==400):
                    rection = pygame.Rect(x*dis, y * dis, dis, dis)
                    pygame.draw.rect(self.window,(0,0,0) , rection,1)
                else:
                    rection = pygame.Rect(x*dis, y * dis, dis, dis)
                    pygame.draw.rect(self.window,(170,170,170) , rection,1)
        self.window.blit(text, (330, 10))
        while 1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    mousex //= dis
                    mousey //= dis
                    mousex *= dis
                    mousey *= dis
                    self.grid(mousex, mousey)
                pygame.display.update()

    def grid(self, x, y, direction=0):
        self.x = x
        self.y = y

        dis = self.size // self.rows
        i = 0
        while 1:
            try:
                dx, dy = directions[direction]
                self.x += dx * dis
                self.y += dy * dis
                a = self.window.get_at((self.x, self.y))
                rect = pygame.Rect(self.x, self.y, dis, dis)
                if a == (0, 0, 0):
                    direction = (direction + 1) % 4  # turn left
                    pygame.draw.rect(self.window, (255, 0, 0), rect, 1)
                elif a == (255, 0, 0):
                    direction = (direction + 3) % 4 # turn right
                    pygame.draw.rect(self.window, (0, 255, 0), rect, 1)

                else:
                    direction = (direction + 3) % 4 # turn right
                    pygame.draw.rect(self.window, (0, 0, 0), rect, 1)

                pygame.display.update()
                i + 1
            except:
                pygame.display.update()
                break

if __name__ == "__main__":
    meg = 800
    reaw = 200
    window = pygame.display.set_mode((meg, meg), (pygame.NOFRAME))
    Mainarw(meg, reaw, window)



# it is not known whether this ant ever produces a highway.