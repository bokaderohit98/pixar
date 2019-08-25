
import numpy as np
import argparse
import cv2
import os


def img_preprocessing(image):
	scaled = image.astype("float32") / 255.0
	lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
	resized = cv2.resize(lab, (224, 224))
	L = cv2.split(resized)[0]
	L -= 50
	return (L, lab)

def predict(net, image):
	L, lab = img_preprocessing(image)
	net.setInput(cv2.dnn.blobFromImage(L))
	ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
	ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
	L = cv2.split(lab)[0]

	colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
	colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
	colorized = np.clip(colorized, 0, 1)
	colorized = (255 * colorized).astype("uint8")

	return colorized

def colorize(net, img_path):
	img = cv2.imread(img_path)
	colorized = predict(net, img)
	new_path = img_path.split('.')[:-1]
	new_path = '.'.join(new_path)
	new_path = new_path + '_intermediate.jpg'
	cv2.imwrite(new_path, colorized)
	return (new_path, colorized)