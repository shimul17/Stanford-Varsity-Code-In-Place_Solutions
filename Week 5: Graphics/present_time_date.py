from graphics import Canvas
from datetime import datetime

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Present time and date
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  
    current_date = now.strftime("%B %d, %Y") 
    current_day = now.strftime("%A")         

    # Background design
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "#1e1e24")
    
    # Effect at middle
    # Border and inside part of card
    canvas.create_rectangle(40, 50, 360, 350, "#2a2b36")
    canvas.create_rectangle(45, 55, 355, 345, "#3e3f4e")
    
    # Time text of clock 
    # To fix at middle 
    canvas.create_text(
        200, 140, 
        text=current_time, 
        font="Courier", 
        font_size=36, 
        color="#00ffd1", 
        anchor="center"
    )
    
    # Divider line
    canvas.create_rectangle(80, 195, 320, 198, "#5a5c75")
    
    # Name of day
    canvas.create_text(
        200, 235, 
        text=current_day, 
        font="Helvetica", 
        font_size=22, 
        color="#ffffff", 
        anchor="center"
    )
    
    # Date in yext
    canvas.create_text(
        200, 280, 
        text=current_date, 
        font="Helvetica", 
        font_size=16, 
        color="#a0a5c0", 
        anchor="center"
    )

if __name__ == '__main__':
    main()
