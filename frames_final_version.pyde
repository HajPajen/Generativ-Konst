from splits import *
from colorful import *
from draws import *
import random


N = 1 #counter for splitting

max_frames = 55 #controls the maximum amount of frames

frames = []
reverse_frames = []
window_width = 600
window_height = 700
edge_length = 20
min_area = (window_width-2*edge_length)*(window_height-2*edge_length)/max_frames #minimum area cannot be smaller than the outer frame's area divided by Nmax

base_palette = create_palette(random_color(random_palette())) #chooses initial palette

def framerate(N,max_frames): #determines framerate based on if frames are splitting or merging and takes the square root of the current amount of frames
    should_split_frames = N < max_frames
    should_merge_frames = max_frames <= N < 2*max_frames-1
    
    if should_split_frames:
        return 2*N**0.5
    elif should_merge_frames:
        return 2*(max_frames-N/2)**0.5

def get_start_frame(): #returns a start frame based on dimensions of window
    global window_width, window_height, edge_length, base_palette
    xmin = edge_length
    xmax = window_width-edge_length
    ymin = edge_length
    ymax = window_height-edge_length
    start_frame = {
        "xmin": xmin,
        "xmax": xmax,
        "ymin": ymin,
        "ymax": ymax,
        "colorid": random_color(base_palette)
        }
    return start_frame

def paint_setup(start_frame): #paints background and shadow
    background(255)
    fill(220,220,220)
    strokeWeight(0)
    rect(start_frame["xmin"]+10,start_frame["ymin"]+7,start_frame["xmax"]-start_frame["xmin"],start_frame["ymax"]-start_frame["ymin"])
    
def setup(): #Sets up window and starting frame
    global frames, window_width, window_height
    size(window_width,window_height)
    start_frame = get_start_frame() 
    frames.append(start_frame) #Adds initial "mother_frame" to start the program based on parameters for frame width and height
    paint_setup(start_frame)

def get_random_pop_index(frames): #chooses random frame to split if the frame is larger than the minimum area and returns the index of said frame
    global min_area
    poppable = False
    while poppable == False:
        boxpop_index = int(random.randint(0,len(frames)-1))
        random_frame = frames[boxpop_index]
        frame_width = random_frame["xmax"]-random_frame["xmin"]
        frame_height = random_frame["ymax"]-random_frame["ymin"]
        area = (frame_width)*(frame_height)
        if area > min_area:
            poppable = True
    return boxpop_index

def select_and_isolate_frame(frames): #Selects the frame and removes it from list of splittable frames
    pop_index = get_random_pop_index(frames)
    frame_to_split = frames[pop_index]
    frames.pop(pop_index)
    return frame_to_split

def split_and_draw(previous_frame): #Splits the selected frame, draws the new frames and saves them in the main frames-list
    global frames, base_palette
    new_frames = splitframes(previous_frame,base_palette)
    draw_frame(new_frames[0])
    draw_frame(new_frames[1])
    frames.append(new_frames[0])
    frames.append(new_frames[1])

def draw_old_frames(reverse_frames): #draws up the old frames once reversing/merging is initialized, working backwards through the saved frames list
    global N, max_frames
    old_frame = reverse_frames[-(N+1-max_frames)]
    recent_color = reverse_frames[-1]["colorid"]
    old_frame["colorid"] = recent_color
    draw_frame(old_frame)
    
def prepare_next_loop(): #Resets frames-list and the reverse-list, keeping the last base-frame and decides on new palette to prepare for the next loop
    global frames, reverse_frames, base_palette
    frames = []
    base_frame = reverse_frames[0]
    base_palette = create_new_palette_based_on(reverse_frames)
    reverse_frames=[]
    frames.append(base_frame)

def draw(): #Main executing function that loops continuously, the events vary based on the amount of frames that have been added/drawn
    global frames, reverse_frames, base_palette, N, max_frames
    should_split_frames  = N < max_frames
    if should_split_frames: 
        frameRate(framerate(N,max_frames))
        frame_to_split = select_and_isolate_frame(frames) #isolate refers to removing the frame so it cannot be split again
        reverse_frames.append(frame_to_split) #saves the frame in separate "reverse-list"
        split_and_draw(frame_to_split)
        N += 1
    else:
        should_merge_frames = max_frames <= N < 2*max_frames-1
        if should_merge_frames:
            frameRate(framerate(N,max_frames))
            draw_old_frames(reverse_frames)
            N+=1
        else:
            prepare_next_loop()
            N = 1
