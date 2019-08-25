import subprocess
import os
import itertools
import threading
import sys
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

done = False
error = False


def animate():
    global done
    global error
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write("\rDownloading Unet " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush()
    if error == False:
        sys.stdout.write("\rUnet Downloaded  ")
        sys.stdout.write("\rSetup Completed  ")
    else:
        sys.stdout.write("\rError Occurred. Unable to complete setup!")


def download_Unet():
    global done
    global error
    try:
        if os.path.exists("./models/Unet/model.caffemodel"):
            print("Unet already exist")
            return

        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        animation_thread = threading.Thread(target=animate)
        animation_thread.start()

        caffeModel = drive.CreateFile({"id": "1RSih3Pv2Q3f0XPnsfFSd8lYbF2lsz9ip"})
        caffeModel.GetContentFile("./models/Unet/model.caffemodel")
    except Exception as error:
        error = True
    finally:
        done = True


def create_client_images_folder():
    try:
        if os.path.exists("./client_images") == False:
            os.mkdir("./client_images")
    except Exception as error:
        print(error)


def main():
    global done
    done = False

    try:
        subprocess.run("pip install -r requirements.txt".split(" "))
    except Exception as error:
        print(error)
    else:
        print("Dependencies Installed")
        download_Unet()
        create_client_images_folder()


if __name__ == "__main__":
    main()

