import requests
from datetime import datetime
import cv2
import argparse
import base64

ap = argparse.ArgumentParser()
ap.add_argument("-i", type=str, nargs="?")
ap.add_argument("-p", type=bool, nargs="?", default=False)
args = vars(ap.parse_args())


def post_img(img_path):
    url = "http://localhost:5000/api"
    if args["p"]:
        url = url + "?pixify=True"
    else:
        url = url + "?pixify=False"

    with open(img_path, "rb") as file:
        files = {"file": file}
        res = requests.post(url, files=files)
        return res


def save_img(encoded):
    decoded = base64.b64decode(encoded)
    filename = (
        "./client_images/" + str(int(datetime.timestamp(datetime.now()))) + ".jpg"
    )

    with open(filename, "wb") as file:
        file.write(decoded)
    return filename


def show_img(filename):
    img = cv2.imread(filename)
    cv2.imshow("Result", img)
    cv2.waitKey(0)


def main():
    res = post_img("./client_images/" + args["i"])
    if res.status_code == 200:
        filename = save_img(res.content)
        show_img(filename)
    else:
        print("Bad Request")


if __name__ == "__main__":
    main()

