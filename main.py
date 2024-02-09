import sys
import os
import pygame
from pygame import mixer
mixer.init()
pygame.init()

window = pygame.display.set_mode((800, 600))

class SoundButton(object):
    def __init__(self, filename, pos) -> None:
        self.pos = list(pos)
        self.filename = filename
        self.text_name = self.filename[:-4]
        self.font = pygame.font.Font(None, 16)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        self.playing = False
        #mixer.music.load(f"sounds/{self.filename}")
        self.sound = mixer.Sound(f"sounds/{self.filename}")
        self.sound.set_volume(0.3)

    def render(self):
        name = self.font.render(self.text_name, (0, 0, 0), False)
        window.blit(name, (self.pos[0], self.pos[1] + self.rect.height + name.get_height()))
        pygame.draw.rect(window, (50, 50, 50), self.rect)
    
    def play(self):
        if self.playing == True:
            control = pygame.key.get_pressed()
            if control[pygame.K_SPACE]:
                self.sound.stop()
                self.playing = False
            else:
                self.sound.play(loops=0)


running = True
buttons = []

if __name__ == "__main__":
    index = 0
    for file in os.listdir("sounds"):
        index += 1
        buttons.append(SoundButton(filename=file, pos=(25 * index * 5, 25)))

while running:
    window.fill((30, 30, 50))
    for button in buttons:
        button.render()
        button.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    print("Playing", button.text_name)
                    button.playing = True

    pygame.display.update()
