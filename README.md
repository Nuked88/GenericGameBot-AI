<div style="width:100%; text-align:center"><img src="https://i.imgur.com/GaRw83d.jpg"></div>

# Python / FastAI CNN - Playing Game
> <del>This code was used to gather and process data while playing the game Fall Guys.</del> 

> This code will be modified for permit to use in every game with a minimum edit of the config.yaml file
> The network was then trained using the FastAI Libary.

> THIS IS A <B>BIG</B> WORK IN PROGRESS

## Setup
- Edit the config.yaml [SEE THE SECTION BELOW]
- Open the game in a small window ( i suggest something 4:3 like 480 x 480 for now)
- Run CreateData.py
- Start changing the value of the region_capured in the config file until the game is perfectly visible in the black window
- Pressing B will start the screen / key grab. These will be stored in lists until you press H.
- Once the episode ( Round ) ends pressing h will stop the screen / key grab process and all data will be moved to a numpy array.The array will be stored in <b>data/target_data_\<nameofthegame\>.npy</b> and <b>data/training_data_\<nameofthegame\>.npy</b>
- Go in Utils folder and run CreateImages.py to generate images that will be splitted in folders corresponding to their actions.The images are stored in <b>images/\<nameofthegame\>/</b>



## Example of a configuration file with explanation
```yaml
game_name:  Tower_Hero #name of the game that will be used for rename the folder and the model (please use underscore intead of space)
path_game: test_path #not used for now
region_captured:  #where the window of the game is located on the screen
  left: 710 #starting point at the left
  top: 300 #starting point at the top
  extensionOfX: 1110 #how far the window of the game extends on the X axis (starting from the left point)
  extensionOfY: 807 #how far the window of the game extends on the Y axis (starting from the top point)
dummmy_direction: LEFT_KEY #direction where to point when you are doing nothing in the game
commands: #association of -key pressed- : -name of the folder where the image will be stored-
  UP_KEY : 'Nothing'
  LEFT_KEY : 'Left'
  DOWN_KEY : 'Down'
  RIGHT_KEY : 'Right'
  ' ' : 'Fire'
```

## Train
- Run training.py


## Run Agents
- Open the game withe the window in the same position of the CreateData.py operation
- Run TrainedAgent.py


<br><br><br><br>
# OLD INSTRUCTION
<code>

## Setup
- I used dual monitors with a game playing at a 800 X 600 resolution on one screen.
- You can start data collection by running CreateData.py
- Pressing B will start the screen / key grab. These will be stored in lists until the episode is done.
- Once the episode ( Round ) ends pressing h will stop the screen / key grab process and all data will be moved to a numpy array.
- Then I used a script in util folder called CreateImages.py to put then onto a disk drive in folders corresponding to their actions.

## Train
- Use the file called training.py
- Point it at your image directory

## Run Agents
- Fully random agent is RandomAgent.py
- Trained Agent is TrainedAgent.py
- You will have to load in the pkl created from training.

## Inputs (Observations)
- Uses inputs to the neural network (Observations) of pixes in the game.
- 224 X 224
- Line detection

## Contact!
- YouTube <a href="https://www.youtube.com/claritycoders" target="_blank">Clarity Coders</a>
- Chat with me! <a href="https://discord.gg/cAWW5qq" target="_blank">Discord</a>
</code>