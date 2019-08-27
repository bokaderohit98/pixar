from .colorize import colorize
from .pixify import pixify
from .loadModels import loadModels
import os


def transform(
    models,
    img_path="input.jpg",
    pixify_image=True,
    delete_intermediate=False,
    delete_input=False,
):
    try:
        unet, rdn = models

        new_path, colorized = colorize(unet, os.path.join("./images/", img_path))
        print("Done Colorizing")

        if pixify_image:
            new_path, result = pixify(rdn, colorized, new_path, delete_intermediate)
            print("Done Pixifying")

    except Exception as error:
        print(error)
        res = "-1"

    else:
        res = new_path

    finally:
        try:
            if delete_input:
                os.remove(os.path.join("./images/", img_path))
        except Exception as error:
            print(error)
        finally:
            return res


if __name__ == "__main__":
    main()
