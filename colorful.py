import random

def random_palette(): #chooses a random palette from list of palettes
    palettes = [
                [(0,139,133), (80,156,228), (8,82,152), (11,44,75)], #greenblue
                [(221,23,23),(251,51,16),(244,13,48),(199,14,14),(214,32,78)], #redpink
                [(38,38,38),(89,89,89),(115,115,115),(158,158,158),(255,255,255)], #"blackwhite
                [(255,210,2),(255,239,175),(255,220,101),(255,220,101),(255,154,0)],#yelloworange
                [(197,227,132),(141,182,0),(217,230,80),(201,220,135),(209,226,49)],#greenlight
                [(255,255,255),(255,255,255),(250,201,1),(35,35,35),(34,80,149),(221,1,0)], #piet mondrian
                [(0,139,133), (80,156,228), (8,82,152), (11,44,75),(221,23,23),(251,51,16),(244,13,48),(199,14,14),(0,0,0),(214,32,78),(255,255,255),(255,210,2),(255,239,175),(255,220,101),(255,220,101),(255,154,0)]
                ]
    palette_choice = palettes[(int(random.randint(0,len(palettes)-1)))]
    return palette_choice


def random_color(palette): #selects random color from a palette
    color_choice = palette[(int(random.randint(0,len(palette)-1)))]
    return color_choice

def create_palette(colour): #creates a palette with added color of choice
    palette = []
    palette.append(colour)
    palette += random_palette()
    return palette

def create_new_palette_based_on(reverse_frames): #creates palette based on most recent color
    recent_color = reverse_frames[-1]["colorid"]
    base_palette = create_palette(recent_color)
    return base_palette
