from flask import Flask, request, send_file, abort, send_from_directory
from flask_cors import CORS
from utils.loadModels import loadModels
from utils.transform import transform
import tensorflow as tf
from datetime import datetime
import numpy as np
import os
import cv2
import base64

app = Flask(__name__, static_folder="build")
CORS(app)


def rename(filename):
    timestamp = datetime.timestamp(datetime.now())
    pieces = filename.split(".")
    return ".".join(pieces[:-1]) + str(int(timestamp)) + "." + pieces[-1]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route("/api", methods=["POST"])
def pixar():
    try:
        pixify_image = request.args.get("pixify")

        if pixify_image == "False":
            pixify_image = False
        else:
            pixify_image = True

        print(request.files)

        img_file = request.files["file"]

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

        with open(res_path, "rb") as file:
            encoded = base64.b64encode(file.read())

        return encoded


if __name__ == "__main__":
    graph = tf.get_default_graph()
    models = loadModels(graph)
    app.run(debug=True, port=5000)

