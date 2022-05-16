import random
from colorful import *

def splitframes(frame,palette): #splits one frame into two smaller ones based on how large the splitter/numerator is
    splitter = random_split_numerator()
    
    frame_width = frame["xmax"]-frame["xmin"]
    frame_height = frame["ymax"]-frame["ymin"]
    
    if frame_width > frame_height:
        direction_split = 0
    elif frame_width < frame_height:
        direction_split = 1
    elif frame_width == frame_height:
        direction_split = int(random.randint(0,1))

    vertical = 0
    horisontal = 1

    if direction_split == vertical:
        split_twins = [
            {
            "xmin": frame["xmin"],
            "xmax": frame["xmin"] + (frame["xmax"]-frame["xmin"])/splitter,
            "ymin": frame["ymin"],
            "ymax": frame["ymax"],
            "colorid": frame["colorid"]
            },
            {
            "xmin": frame["xmin"] + (frame["xmax"]-frame["xmin"])/splitter,
            "xmax": frame["xmax"],
            "ymin": frame["ymin"],
            "ymax": frame["ymax"],
            "colorid": random_color(palette)
            }
        ]
    elif direction_split == horisontal:
        split_twins = [
            {
            "xmin": frame["xmin"],
            "xmax": frame["xmax"],
            "ymin": frame["ymin"],
            "ymax": frame["ymin"]+(frame["ymax"]-frame["ymin"])/splitter,
            "colorid": frame["colorid"]
            },
            {
            "xmin": frame["xmin"],
            "xmax": frame["xmax"],
            "ymin": frame["ymin"]+(frame["ymax"]-frame["ymin"])/splitter,
            "ymax": frame["ymax"],
            "colorid": random_color(palette)
            }
        ]
    return split_twins

def random_split_numerator(): #returns a random splitter/numerator from a list of numerators
    numerators = [1.25,1.75,2,3,4]
    numeratr_choice = numerators[(int(random.randint(0,len(numerators)-1)))]
    return numeratr_choice
