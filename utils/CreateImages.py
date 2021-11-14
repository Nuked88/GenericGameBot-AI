import cv2
import numpy as np
from pathlib import Path
import yaml

Debug = False
main_path = Path(__file__).parent.parent

# Load Config
config_path = f"{main_path}\\config.yaml"

with open(config_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
# End Load Config

# Get game name
game_name = config['game_name']
# List of commands and their corresponding folder names
dict_commands = config['commands'] 


#set data and target vars
data = np.load(f"{main_path}\\data\\training_data_{game_name}.npy", allow_pickle=True)
targets = np.load(f"{main_path}\\data\\target_data_{game_name}.npy", allow_pickle=True)

#print(f'Image Data Shape: {data.shape}')
#print(f'targets Shape: {targets.shape}')


# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

print(f'Total number of moves: {len(holder_list)}')

#Create a folder for each command.
for folder in dict_commands:
    print(f'Creating folder: {main_path}\\images\\{game_name}\\{dict_commands[folder]}')
    Path(f'{main_path}\\images\\{game_name}\\{dict_commands[folder]}').mkdir(parents=True, exist_ok=True)

count = {}
for data in holder_list:

    #if is present in command list, then imwrite.
    try:
        name_folder=dict_commands[data[1]]
        fist_letter_name_lower = name_folder[0].lower()
        path_image=f'{main_path}\images\\{game_name}\\{name_folder}\\H7-{fist_letter_name_lower}{count.get(name_folder,0)}.jpg'
        cv2.imwrite(path_image, data[0])
        count[dict_commands[data[1]]] = count.get(dict_commands[data[1]], 0) + 1

    except:
        if Debug:
           print(f'Skip for {data[1]}')

print("Counts:")
for key in count:
    print(f'{key}: {count[key]}')
