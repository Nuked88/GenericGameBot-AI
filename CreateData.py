import numpy as np
import cv2
import time
import os
import yaml
from pathlib import Path
from utils.grabscreen import grab_screen
from utils.getkeys import key_check


main_path = Path(__file__).parent

# Load Config
config_path = f"{main_path}\\config.yaml"

with open(config_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

game_name = config['game_name']

rc = config['region_captured']


# Define data folder
training_data_folder = f"{main_path}\\data\\training_data_{game_name}.npy"
target_data_folder = f"{main_path}\\data\\target_data_{game_name}.npy"


def get_data():

    if os.path.isfile(training_data_folder):
        print('File exists, loading previous data!')
        image_data = list(np.load(training_data_folder, allow_pickle=True))
        targets = list(np.load(target_data_folder, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(training_data_folder, image_data)
    np.save(target_data_folder, targets)


def imageInitializer():
    #left, top, x2, y2 
    image = grab_screen(region=(rc["left"], rc["top"], rc["extensionOfX"], rc["extensionOfY"]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=119, threshold2=250)
    image = cv2.resize(image, (300, 198))

    # Debug line to show image
    cv2.imshow("AI Peak", image)
    cv2.waitKey(1)
    return image


image_data, targets = get_data()
while True:
    # Keep reaload config
    with open(config_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    rc = config['region_captured']

    imageInitializer()

    keys = key_check()
    print(f"waiting press B to start, pressed: {keys}")
    if keys == "B":
        print("Starting")
        break


count = 0
while True:
    count +=1
    last_time = time.time()

    image = imageInitializer()

    # Convert to numpy array
    image = np.array(image)
    image_data.append(image)

    keys = key_check()
    targets.append(keys)
    if keys == "H":
        break

    print('loop took {} seconds'.format(time.time()-last_time))

save_data(image_data, targets)
