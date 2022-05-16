
def draw_frame(frame): #draws the frame based on it's characteristics given in dictionary

    strokeWeight(3.25)
    frame_color = frame["colorid"]
    fill(frame_color[0],frame_color[1],frame_color[2])
    rect(int(frame["xmin"]),int(frame["ymin"]),int(frame["xmax"]-frame["xmin"]),int(frame["ymax"]-frame["ymin"]))
    

    
