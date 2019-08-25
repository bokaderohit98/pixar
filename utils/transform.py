from .colorize import colorize
from .pixify import pixify
from .loadModels import loadModels
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--img", type=str, default='input.jpg', help="path to input black and white image", nargs='?')
ap.add_argument("-dim", type=bool, default=False, help="delete intermediate output?", nargs='?')
ap.add_argument("-din", type=bool, default=False, help="delete input image?", nargs='?')
args = vars(ap.parse_args())

def transform(models, img_path='input.jpg', delete_intermediate=False, delete_input=False):
    try:
        # unet, rdn = models
        unet = models
        new_path, colorized = colorize(unet, os.path.join('./images/', img_path))
        print('Done Colorizing')
        # new_path, result = pixify(rdn, colorized, new_path, delete_intermediate)
        # print('Done Pixifying')
    except Exception as error:
        print(error)
        res = "-1"
    else:
        res = new_path
    finally:
        try:
            if delete_input:
                os.remove(os.path.join('./images/', img_path))
        except Exception as error:
            print(error)
        finally:
            return res

def main():
    models = loadModels()
    transform(models, args['img'], args['dim'], args['din'])

if __name__ == '__main__':
    main()