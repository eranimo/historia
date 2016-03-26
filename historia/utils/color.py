from colour import Color
from random import randint

def random_country_colors():
    map_color = Color(hue=randint(0, 255), saturation=0.5, luminance=0.5)
    border_color = Color(map_color, luminance=0.33)
    return map_color, border_color
