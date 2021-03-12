import pygame as pg
import random
class MatrixLetters:
    def __init__(self, app):
        self.app = app
        self.letters = [chr(int('0x30a0', 16) + i) for i in range(1, 95)]
        self.font_size = 12
        self.font = pg.font.SysFont('ms mincho', self.font_size, bold=True)
        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (2, 245, 27))
            pos = i * self.font_size, self.drops[i] * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0,1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw()

class MatrixApp:
    def __init__(self): # инициализация приложения
        self.RES = self.WIDTH, self.HEIGHT = 1000, 700
        pg.init()
        self.screen = pg.display.set_mode(self.RES)  #отображаемый экран
        self.surface = pg.Surface(self.RES, pg.SRCALPHA) # поверхность отрисовки
        self.clock = pg.time.Clock()  # для отслеживания времени
        self.matrixLetters = MatrixLetters(self)

    def draw(self):#закраска рабюповерхности и нанесем на гл.экран
        self.surface.fill((0,0,0,10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self): #главный цикл программы
        while True:
            self.draw()  #jnhbcjdrf 'rhfyf
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip() #обновление поверхности
            self.clock.tick(30) # установка кадров


if __name__ == '__main__':
    app = MatrixApp()
    app.run()