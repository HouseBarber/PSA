from src.library.vector.vector import Vector
import pygame
from src.library.pygame.pygame import PygameEngine

class Object:

    def __init__(self):
        self.pygame_engine = PygameEngine()
        self.sprite = None
        self.sprites: list[pygame.Surface] = []  # Lista de sprites
        self.size = [0, 0]
        self._speed = Vector(0, 0)
        self.position = Vector(0, 0)
        self.meters_to_pixel = 20

    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        max_x = (screen_width / self.meters_to_pixel) - \
            (self.size[0] / self.meters_to_pixel)
        max_y = (screen_height / self.meters_to_pixel) - \
            (self.size[1] / self.meters_to_pixel)

        max_x = max(0, max_x)
        max_y = max(0, max_y)

        self.position.x += self._speed.x * delta_time
        self.position.y += self._speed.y * delta_time

        self.position.x = max(0, min(self.position.x, max_x))
        self.position.y = max(0, min(self.position.y, max_y))


    def get_current_sprite(self) -> pygame.Surface:
        return self.pygame_engine.scale_sprite(self.sprite, self.size[0], self.size[1])


    def draw_object(self, screen) -> None:
        sprite = self.get_current_sprite()
        if sprite:
            screen.blit(sprite, (self.position.x *
                self.meters_to_pixel, self.position.y * self.meters_to_pixel)
            )
            
    
    def explosion(self, sprite: str):
        self.sprite = self.pygame_engine.load_sprite_image(sprite)
        self.sprite = self.pygame_engine.scale_sprite(
            self.sprite, self.size[0], self.size[1]
        )
        
        
    def stop_movement(self) -> None:
        self._speed = Vector(0, 0)
