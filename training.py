from fastai.vision.all import *
import time
import cv2
import yaml
from utils.grabscreen import grab_screen
from pathlib import Path

main_path = Path(__file__).parent

# Load Config
config_path = f"{main_path}\\config.yaml"
with open(config_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

game_name = config['game_name']
rc = config['region_captured']

def label_func(x): return x.parent.name

def run():
    path = Path(f'{main_path}\\images\\{game_name}\\')
    fnames = get_image_files(path)
    print(f"Total Images:{len(fnames)}")


    dls = ImageDataLoaders.from_path_func(path, fnames, label_func,bs=40, num_workers=0)
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    learn.model.cuda()
    print("Loaded")
    learn.fine_tune(40, base_lr=1.0e-02)

    learn.export(f'{main_path}\\models\\{game_name}.pkl')
    
    # start_time = time.time()
    # test = learn.predict('g1-j5.png')
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print(test)
    start_time = time.time()
    image = grab_screen(region=(rc["left"], rc["top"], rc["extensionOfX"], rc["extensionOfY"]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image, (224, 224))
    test = learn.predict(image)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(test)


if __name__ == '__main__':
    run()