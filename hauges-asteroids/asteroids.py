from os import kill

import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update the asteroid's position based on its velocity and dt
        self.position += self.velocity * dt

    def split(self) -> list['Asteroid']:
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle_split = random.uniform(20, 50)
        old_radius = self.radius
        new_velocity1 = self.velocity.rotate(angle_split)
        new_velocity2 = self.velocity.rotate(-angle_split)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = new_velocity1 * 1.2
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = new_velocity2 * 1.2
        return [first_asteroid, second_asteroid]
        