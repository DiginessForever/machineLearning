import numpy, glob, os, math

class neuralnetwork:
	layers = []
	weightMatrix = []

	n = 1000  #How accurate do we want to take the exponential function (below) - we use the exponential function as the activation function
	e = (1.0 + 1.0/n)^n

	def __init__ (self, layersList):
		count = 0
		for layer in layersList: 
			lastLayer = layer
			self.layers.append(initLayer(layer))
			if count > 0:
				self.weightMatrix.append(lastLayer, layer)
			count++

	def initLayer(numberOfNeurons):
		matrix = numpy.random.rand(numberOfNeurons) #This will make a one-dimensional array filled with random values.
		return matrix

	def generateLayerWeightsBetweenLayers(layer, nextLayer):
		matrix = numpy.random.rand(len(layer), len(nextLayer))
		return matrix

	#Rectified Linear Unit activation function.
	#BIt outputs zero as long as x is zero, and outputs x when x is >= 0.
	def reluActivationFunction(x):
		return numpy.maximum(x, 0)

	def forwardPropagate(self):
		count = 0
		for layer in self.layers:
			#Do the multiplication of each neuron by all the weights between it and the next layer,
			#using the layers matrix and the weightMatrix.  Use numpy matrix multiplication for this...somehow.

	def backPropagate(self):
		count = 0
		for layer in self.layers:
			#Go backward, much like above, but you have to do the derivative, taking into account the difference
			#between the output layer and the training model/class.
