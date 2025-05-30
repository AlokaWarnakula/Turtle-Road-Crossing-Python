Turtle Road Crossing Game
A Python Turtle-based arcade game where you navigate a turtle across a road filled with moving cars, featuring a checkered light gray road with dark gray borders, level progression, and collision detection.
Overview
This project is a keyboard-controlled road crossing game built using Python's Turtle module. Guide a black turtle from the bottom to the top of a 600x600 pixel canvas, avoiding randomly spawned cars. The road features light gray blocks in a checkered pattern, framed by dark gray borders. The game includes a scoreboard, increasing car speeds per level, and a game-over condition on collision.
Screenshots
Screenshots are located in the TurtleRoadCrossing directory:

TurtleRoadCrossing/1.png: Game start with turtle at the bottom
TurtleRoadCrossing/2.png: Mid-game with turtle crossing and cars moving
TurtleRoadCrossing/3.png: Game over screen with "Turtle Died" message


Features

Player Control: Move a black turtle up/down using arrow keys.
Dynamic Cars: Cars spawn randomly (1/6 chance per frame) with colors (red, orange, yellow, green, blue, purple) and move left, speeding up each level.
Road Design: Checkered pattern with light gray blocks (30px tall, 300px wide) and dark gray borders (20px tall, 600px wide) at y=280 and y=-280.
Scoreboard: Displays current level and "Turtle Died" on collision.
Game Loop: Updates every 0.1 seconds, handling collisions and level progression.

Controls



Key
Action



Up
Move turtle up 10 pixels


Down
Move turtle down 10 pixels


Installation

Clone the repository:git clone https://github.com/your-username/turtle-road-crossing.git


Navigate to the project directory:cd turtle-road-crossing/TurtleRoadCrossing


Run the game (Python 3.6+ required):python main.py



File Structure
turtle-road-crossing/
├── TurtleRoadCrossing/
│   ├── main.py             # Main game loop and setup
│   ├── road_drawing.py     # RoadDrawer class for checkered road and borders
│   ├── car_manager.py      # CarManager class for car spawning and movement
│   ├── player.py           # Player class for turtle controls
│   ├── scoreboard.py       # Scoreboard class for level and game-over display
│   ├── 1.png               # Screenshot: Game start
│   ├── 2.png               # Screenshot: Mid-game
│   ├── 3.png               # Screenshot: Game over
└── README.md               # Project documentation

How It Works

Main Script (main.py): Initializes a 600x600 pixel Turtle screen, sets up game objects, and runs a loop with 0.1-second updates.
RoadDrawer (road_drawing.py): Draws light gray road blocks (30px tall, 300px wide) at specified y-positions and dark gray borders (20px tall, 600px wide) at y=280 and y=-280.
CarManager (car_manager.py): Spawns cars at random y-positions (-250 to 250) with a 1/6 chance, moving left at increasing speeds.
Player (player.py): Controls a black turtle starting at (0, -280), moving 10 pixels up/down, resetting on crossing y=280.
Scoreboard (scoreboard.py): Displays level at (-230, 270) and "Turtle Died" at (0, 0) on collision.

Requirements

Python 3.6+ (Turtle module included in standard library)
No external dependencies

Acknowledgements
The core game concept was inspired by a Python programming course, which provided the basic requirements for a road crossing game. I implemented the game independently, designing the checkered light gray road and dark gray borders to enhance the visual and gameplay experience.
Future Improvements

Add sound effects for collisions or level-ups
Introduce varied car speeds or types
Implement power-ups or obstacles
Add a high-score system
Allow turtle color customization

License
MIT License — free to use, modify, and distribute.

Happy crossing! 🐢🚗
