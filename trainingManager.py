import sys
import numpy
import imageImport
from pythonReluNeuralNet import *

#Going to try to train the network for a single object class to find in images:
def trainMyNetwork(imageListPositives, imageListNegatives, maxImageSize):
	print("entering trainMyNetwork, maxImageSize is " + str(maxImageSize))
	nn = NeuralNetwork()
	#layerSize = maxImageSize * imagesInBatch
	layerSize = maxImageSize[0] * maxImageSize[1] * 3 #(width * height * 3 because each pixel has three color values)
	nn.addLayer(layerSize) #add the input layer

	#Add more layers:
	layerSize = len(nn.layers[0].neurons)
	print("layerSize: " + str(layerSize))
	nn.addLayer(10000) #10K neurons
	nn.addLayer(8000)
	nn.addLayer(6000)
	nn.addLayer(4000)
	nn.addLayer(2000)
	nn.addLayer(1000)
	nn.addLayer(500)
	nn.addLayer(250)
	nn.addLayer(100)
	nn.addLayer(50)
	nn.addLayer(25)
	nn.addLayer(10)
	nn.addLayer(2)
	'''
	while layerSize >= 2:
		lastLayerIndex = len(nn.layers) - 1
		lengthOfLastLayer = len(nn.layers[lastLayerIndex].neurons)
		#I'm going to have two classes for my first attempt:
		#A positive and a negative certainty.
		#If the positive is high, the network thinks it's this class.
		#If the negative is high, the network thinks it's not this class.
		#If they're both middling, I'm going to kick the network in the groin.
		if lengthOfLastLayer > 22:
			nn.addLayer(lengthOfLastLayer - 20)
		else:
			nn.addLayer(2)
	'''
	print("nn has " + str(len(nn.layers)) + " layers.")
	for layer in range(0, len(nn.layers)):
		layer = nn.layers[layer]
		neurons = layer.neurons
		print("layer" + str(layer) + " has " + str(len(neurons)) + " neurons.")

	#Time to train:
	#for index in range(0, numberOfBatches):
	#	nn.layers[0] = imageImport.createBatch(imageList, imagesInBatch)

	#

def main():
	from sys import argv
	#print(argv)
	if (len(argv) > 1):
		argList = argv[1].split('/')
		imagePath = argList[0]
		className = argList[1]
	else:
		raise ValueError("Usage: python trainingManager.py images/<className>")

	size = 64, 64
	positiveImageList = imageImport.imageImport(imagePath, className, size)
	#getNegativeSamples(imgSizeDesired, numberOfSamples, positiveClassName) #these are the arguments needed for that method
	positiveClassName = "./images/" + className
	negativeImagelist = imageImport.getNegativeSamples(size, 1000, positiveClassName)
	trainMyNetwork(positiveImageList, negativeImagelist, size)
	
	#myNet = trainMyNetwork(positiveImageList, negativeImagelist, maxImageSize)

	#for layerNum in range(0, len(nn.layers)):
	#	print("Layer " + str( layerNum) + " has " + str(len(nn.layers[layerNum].neurons)) + " neurons.")

if __name__ == "__main__":
	main()