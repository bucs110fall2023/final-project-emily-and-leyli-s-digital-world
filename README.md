[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803289&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

Mascot Massacre
## CS110 Final Project  << Fall, 2023 >>

## Team Members

Emily Jiang & Leyli Zeynalova

***

## Project Description

An interactive shooting game, where the goal is to hit the other school's mascots (Stony Brook & University of Buffalo) 
The player has one minute to shoot as many mascots while the game actively logs the player's score and general high scores.
There is a point system implemented for shooting certain mascots, and one powerup avaliable to obtain on the Stony Brook's mascot It spawns in with a paper ball on its shirt and adds an addtional three paper balls to shoot with.  

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design
### Features
1. << Cursor Movement >>
2. << Moving Images >>
3. << Shooting Mechanic >>
4. << Updating Score >>
5. << Special Targets >>

### Classes

- << You should have a list of each of your classes with a description >>
Controller Class Description:
The controller class initializes the game, managing its states such as the main menu, gameplay, and game over screens, and handles user input. The class controls the updating and rendering of game elements, including mascots, the background, user interface components, and displaying the scores and timers.

Highscore.Json:
File that holds the highest score

Menu Class Description: 
Represents a menu object, designed to be used as a sprite in a game, and has the functionality needed for displaying menu items.

SBMascot Class Description:
Pygame sprite represents a Stony Brook mascot in our game. It initializes variables like position and images. The mascot moves horizontally across the screen, and if it goes off the screen, a new mascot is added on the opposite side. Based off of the appearance, each kind of mascot has its own point value, and a chance of spawning a power-up. The class is intended for use in a game loop to update and draw the mascot.

UBMascot Description: 
Pygame sprite represents a University at Buffalo (UB) mascot in our game. The mascot moves horizontally across the screen, and if it goes off the screen, a new mascot is added on the opposite side. The class is intended for use in a game loop to update and draw the mascot.

Main Class Description:
Initializes Pygame, creates a game controller object (Controller), and starts the main game loop by calling the mainLoop method on the controller.

## ATP

Test Case 1: Cursor Movement
Test Description: Verify that a cursor appears on screen
Test Steps: 
1- Run the game
2- Move the mouse around 

Expected Outcome: Cursor has an aim icon and is tracked across the screen

Test Case 2: Moving Images
Test Description: Confirm that images appear to move across the screen

Test Steps:
1- Run the game
2- Wait to see if icons move across the screen

Expected Outcome: Images of the schools mascots move across the screen

Test Case 3: Shooting Mechanic
Test Description: When you hit the mascots they are "shot" and no longer appear on screen 
Test Steps:
1- Run the game
2- Move the cursor over one of the mascot targets
3- Press the mousebutton 
4- See if the mascot disappears off the screen and increases the score count

Expected Outcome: Hitting the school mascots takes them off the screen and updates the score

Test Case 4: Updating Score
Test Description: Score number values that appear reflect the points earned by playing the game
Test Steps:
1- Run the game
2- Move the cursor over one of the mascot targets
3- Press the mousebutton 
4- See if the mascot disappears off the screen 
5- Check if the score on the top left updates and relfects the points earned

Expected Outcome: Score updates on screen based off of hitting certain mascots

Test Case 5: Special Targets
Test Description: Certain mascots move across the screen and have targets painted on them at random
Test Steps:
1- Run the game
2- Wait to view if different variations of the mascots appear on screen, some being with the targets and some without

Expected Outcome: Randomly has mascots with targets that are worth more and reflected in the score

