# Instructions

## Downloading

The game can be downloaded from the [Releases page](https://github.com/PatrickSalmi/Tower-defence-game/releases)

## Installation and starting the game

1. Install dependencies:
```
poetry install
``` 
2. Start the game:
```
poetry run invoke start
```

## Controls

- the game is controlled using a mouse.
- press play to start a game.
- all of the controls are on the right side of the screen.

![game_screen](https://github.com/PatrickSalmi/Tower-defence-game/blob/master/documentation/pictures/game_screen.png)

- to buy a tower, click on it and then click on the game screen to place it.
- to sell a tower, click on the sell button and it will turn red, then click on a tower to sell it.
- to stop selling, click on the sell button again and it will return to it's original color.
- the play/pause button pauses and unpauses the game.
- clicking on retire will end the game and open the score screen where you can see your score.


## How to play

- once the game begins enemies will start to travel along the path from the left side of the screen and attempt to travel to the end of the path
- the objective is to not let any enemies get to the end
- if they do you will lose health and if your health goes to zero the game is over
- towers can be purchased with money which is earned by killing enemies
- when placing a tower the circle around it shows it's attck range
- once a tower is placed it will begin to attack enemies it can reach
- winning the game requires you to survive all waves showed in the top right corner

## Scores
- your total score is saved automatically and can be viewed from the scores menu
