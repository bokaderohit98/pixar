from flask import Flask, request, send_file, abort
from utils.loadModels import loadModels
from utils.transform import transform
import tensorflow as tf
from datetime import datetime
import numpy as np
import os
import cv2

app = Flask(__name__)


def rename(filename):
    timestamp = datetime.timestamp(datetime.now())
    pieces = filename.split(".")
    return ".".join(pieces[:-1]) + str(int(timestamp)) + "." + pieces[-1]


@app.route("/api", methods=["POST"])
def pixar():
    try:
        pixify_image = request.args.get("pixify")

        if pixify_image == "False":
            pixify_image = False
        else:
            pixify_image = True

        img_file = request.files["img"]
        filename = img_file.filename
        filename = rename(filename)

        if os.path.exists("./images") == False:
            os.mkdir("./images")

        img_file.save(os.path.join("./images", filename))

    except Exception as error:
        print(error)
        return abort(400)

    else:
        res_path = transform(
            models, filename, pixify_image, delete_input=True, delete_intermediate=True
        )
        if res_path == "-1":
            return abort(404)
        return send_file(res_path, mimetype="image/jpeg")


if __name__ == "__main__":
    graph = tf.get_default_graph()
    models = loadModels(graph)
    app.run(debug=True, port=3000)

