import cv2
# from models.RDN.rdn import RDN
import numpy as np

def loadUnet():
	proto_txt = './models/Unet/architecture.prototxt'
	model = './models/Unet/model.caffemodel'
	points = './models/Unet/points.npy'
	net = cv2.dnn.readNetFromCaffe(proto_txt, model)
	pts = np.load(points)

	class8 = net.getLayerId("class8_ab")
	conv8 = net.getLayerId("conv8_313_rh")
	pts = pts.transpose().reshape(2, 313, 1, 1)
	net.getLayer(class8).blobs = [pts.astype("float32")]
	net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

	return net

def loadRDN():
  rdn = RDN(arch_params={'C': 6, 'D':20, 'G':64, 'G0':64, 'x':2})
  rdn.model.load_weights('./models/RDN/weights.hdf5')

  return rdn

def loadModels():
  # return (loadUnet(), loadRDN())
	return loadUnet()