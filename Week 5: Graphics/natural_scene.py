from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    # draw two more clouds, and three trees
    draw_cloud(canvas, 20, 40, 'lightcoral')
    draw_cloud(canvas, 270, 20, 'peachpuff')
    
    # Three tree
    draw_tree(canvas, 40, 'darkgreen')
    draw_tree(canvas, 120, 'red')
    draw_tree(canvas, 300, 'yellow')

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

# for trees, as well as for any extra elements in the scene.
def draw_tree(canvas, x, leaves_color):
    """
    Draws one tree anchored to TREE_BOTTOM_Y.
    x represents the leftmost coordinate of the tree's leaves.
    """
    # Calculate trunk coordinates relative to the tree bottom
    trunk_x1 = x + (LEAVES_SIZE / 2) - (TRUNK_WIDTH / 2)
    trunk_y1 = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_x2 = trunk_x1 + TRUNK_WIDTH
    trunk_y2 = TREE_BOTTOM_Y
    
    # Draw brown trunk
    canvas.create_rectangle(
        trunk_x1, 
        trunk_y1, 
        trunk_x2, 
        trunk_y2, 
        'saddlebrown'
    )
    
    # Draw green foliage sitting on top of the trunk
    leaves_x1 = x
    leaves_y1 = trunk_y1 - (LEAVES_SIZE / 2)
    leaves_x2 = x + LEAVES_SIZE
    leaves_y2 = trunk_y1 + (LEAVES_SIZE / 2)
    
    canvas.create_oval(
        leaves_x1, 
        leaves_y1, 
        leaves_x2, 
        leaves_y2, 
        leaves_color
    )
  
if __name__ == '__main__':
    main()
