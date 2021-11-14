import random
import time
import yaml
from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2

from pathlib import Path
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *


main_path = Path(__file__).parent

# Load Config
config_path = f"{main_path}\\config.yaml"
with open(config_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

game_name = config['game_name']
rc = config['region_captured']
# List of commands and their corresponding folder names
dict_commands = config['commands'] 


def label_func(x): return x.parent.name
learn_inf = load_learner(f"{main_path}\\models\\{game_name}.pkl")
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Hold down W no matter what!
keyboard.press('w')

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump

while True:

    image = grab_screen(region=(rc["left"], rc["top"], rc["extensionOfX"], rc["extensionOfY"]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    #print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())

    #action = random.randint(0,3)
    
    if action == "Down" or result[2][0]>.1:
        print(f"Down! - {result[1]}")
        keyboard.press("down")
        keyboard.release("left")
        keyboard.release("right")
        keyboard.release("up")
        time.sleep(sleepy)

    if action == "Nothing":
        #print("Doing nothing....")
        keyboard.press("up")
        keyboard.release("left")
        keyboard.release("right")
        keyboard.release("down")

        time.sleep(sleepy)

    elif action == "Left":
        print(f"LEFT! - {result[1]}")
        keyboard.press("left")
        keyboard.release("right")
        keyboard.release("down")
        keyboard.release("up")
        time.sleep(sleepy)

    elif action == "Right":
        print(f"Right! - {result[1]}")
        keyboard.press("right")
        keyboard.release("left")
        keyboard.release("down")
        keyboard.release("up")
        time.sleep(sleepy)


    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break

keyboard.release('left')