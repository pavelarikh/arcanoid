from dataclasses import dataclass


@dataclass
class Settings():
    width_window: int = 1500
    length_window: int = 1000
    name: str = 'it\'s a arcanoid game'
    backround_color: tuple = (32, 178, 170)
    fps: int = 40