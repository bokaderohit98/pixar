import cv2
import os

def pixify(rdn, img, img_path, delete_intermediate=False):
    print('starting')
    result = rdn.predict(img)
    print('pixified')
    if delete_intermediate:
        os.remove(img_path)

    new_path = img_path.split('_')[:-1]
    new_path = '_'.join(new_path)
    new_path = new_path + '_result.jpg'
    cv2.imwrite(new_path, result)

    return new_path, result
