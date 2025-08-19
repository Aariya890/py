import math
import random
import sys
from dataclasses import dataclass
import pygame

WIDTH, HEIGHT = 960, 600
FPS = 60
STAR_LAYERS = [(90, 1), (60, 2), (30, 3)]
PLAYER_SPEED = 6
BULLET_SPEED = 12
BULLET_COOLDOWN = 220
ENEMY_SPAWN_BASE = 1100
ENEMY_SPAWN_MIN = 400
LEVEL_UP_EVERY = 20
BLACK = (10, 10, 14)
WHITE = (240, 240, 240)
GREY = (120, 120, 140)
RED = (220, 60 ,70)
GREEN = (70, 120, 200)
YELLOW = (240, 210, 80 )
CYAN = (90, 200, 230)
ORANGE = (255, 150, 60)
PURPLE = (180, 110, 220)

def clamp(v, lo , hi):
    return max(lo, min(hi, v))

@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    life: float
    color: tuple
    size: float
    
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt
    
    def draw(self, surf):
        if self.life <= 0:
            return
        alpha = int(255 * clamp(self.life, 0, 1))
        s = max(1, int(self.size))
        particle = pygame.Surface((s, s), pygame.SRCALPHA)
        pygame.draw.circle(particle, (*self.color, alpha), (s // 2, s // 2), s // 2)
        surf.blit(particle, (self.x - s // 2, self.y - s // 2))