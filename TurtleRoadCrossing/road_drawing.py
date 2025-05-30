from turtle import Turtle

# Adjusted BLOCK_LOCATION for checkered pattern with gaps
BLOCK_LOCATION = [
    (0, 250), (0, 190), (0, 130), (0, 70), (0, 10),  # First set of black boxes
    (0, -50), (0, -110), (0, -170), (0, -230), (0, -290)  # Second set
]

class RoadDrawer:
    def __init__(self):
        self.road_blocks = []

    def blockGenerate(self):
        for pos in BLOCK_LOCATION:
            roadBlock = Turtle()
            roadBlock.shape("square")
            roadBlock.color("lightgray")
            roadBlock.penup()
            roadBlock.goto(pos)
            roadBlock.shapesize(stretch_wid=1.5, stretch_len=15)
            self.road_blocks.append(roadBlock)