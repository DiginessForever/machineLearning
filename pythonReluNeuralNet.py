import numpy as np
import glob, os

class NeuralNetwork:
	class Layer:
		class Neuron:
			netValue = 0.
			activationValue = 0.
			weights = [] # each neuron should have weights for each of the neurons in the layer before it
			weightsAfterErrorSubtracted = []
			incomingError = 0.

			def __init__(self, numberOfWeights):  #note - an input layer neuron will have no weights
				weights = np.rand(numberOfWeights)

		neurons = [] #1xN matrix, where N = number of neurons in this layer.  Each neuron is a float value between 0 and 1.
						#This holds the "activation" values, which are the sum of activations in the previous layer times the weights.

		totalLayerError = 0.  	#used for the backprop, this is the sum of (actual - expected) * sigmoidDerivative(actual) for all outputs.
								#or for hidden layers, it's the sum of the above * each of the neuron activations (outputs).
		
		def __init__(self, numberOfNeurons, numberOfWeightsPerNeuron):
			for neuron in range(0, numberOfNeurons):
				self.neurons.append(Neuron(numberOfWeightsPerNeuron))

	layers = []
	totalError = 999. #some big number when we first init
	outputErrorDerivatives = []
	learningRate = 0.5
	classNames = [] #These will be strings which correspond to neurons in the output layer.  Each neuron will represent an object type.
					#The strings will be the names of those object types.  The values in those output layer neurons will be the level
					#of certainty the neural net has assigned to the input belonging to one of those classes.

	def __init__(self):
		#empty - none of the properties are set yet in this constructor.

	def addLayer(self, numberOfNeuronsInLayer):
		numberOfNeuronsInLastLayer = 0.
		#Each neuron in this layer should have a weight to every neuron in the layer prior:
		if (self.layers.len > 0):
			lastLayerIndex = self.layers.len - 1
			numberOfNeuronsInLastLayer = self.layers[lastLayerIndex]
		layer = Layer(numberOfNeuronsInLayer, numberOfNeuronsInLastLayer)
		self.layers.append(layer)

	def doTrainEpoch(self, input, expectedOutput):
			forwardPropagateNetwork(input)
			calculateTotalError(input, expectedOutput)
			backpropagateNetwork()
			applyBackproppedWeightChanges()

	#I found a good reference for doing propagation with numpy.dot multiplication here:
	#https://databoys.github.io/Feedforward/
	def forwardPropagateNetwork(self):
		for layer in range(0, self.layers.len - 2):  #not going to forward prop from the output layer, so we stop at one before it.
			activations = []
			for neuron in self.layers[layer].neurons:
				activations.append(neuron.activationValue)
			for neuron in self.layers[layer + 1].neurons:
				neuron.netValue = np.dot(activations, neuron.weights)  #spiffy optimized function that multiplies them all together in order and sums them up.
				neuron.activationValue = sigmoid(neuron, False) #run the activation function on the neuron for the final value - second arg is false because we aren't backpropping

	def calculateError(self, expectedOuput, actualOutput):
		if (expectedOuput.len != actualOutput.len):
			print "Expected and Actual Output lengths do not match."
			return

		self.totalError = 0.
		self.outputErrorDerivatives = []
		for output in range(0, expectedOuput):
			self.totalError +=  .5*(actualOutput - expectedOutput)**2
			self.outputErrorDerivatives.append(actualOutput - expectedOutput)

		#Setup the error on the output neurons for the backprop:
		outputLayer = self.layers[self.layers.len - 1]
		for output in range(0, self.outputErrorDerivatives.len - 1):
			error = self.outputErrorDerivates[output]
			outputLayer.neurons[output].incomingError = error * sigmoid(error, True)

	def backpropagateNetwork(self):
		for layer in range(self.layers.len - 1, 1, -1): #we don't backprop all the way to the input layer because that layer doesn't have its own weights
														#I visualize weights as belonging to the layer to the right, with the input layer all the way to the left.
			nextLayer = layer - 1
			backpropFromThisLayerToNextLayer(layer, nextLayer)

	def backpropFromThisLayerToNextLayer(self, thisLayer, nextLayer):
		newWeightsInNextLayer = []
		#for neuron in thisLayer.neurons:

		for outNeuron in nextLayer.neurons:
			incomingErrorSum = 0.
			for inNeuron in thisLayer.neuron:
				incomingErrorSum += learningRate * inNeuron.incomingError * outNeuron.activationValue
			outNeuron.incomingError = incomingErrorSum
			#we'll subtract these values from the weights in the next layer once we
			#are completely done with the backprop all the way through all the layers.

	def applyBackproppedWeightChanges(self):
		for layer in range(1, self.layers - 1):
			for neuron in layer.neurons:
				for weight in neuron.weights:
					weight = weight - neuron.incomingError

			
	def printTop5Results(self):
		print "Implement your print function, mister!"


	n = 1000  #How accurate do we want to take the exponential function (below) - we use the exponential function in the activation function.
	e = (1.0 + 1.0/n)^n  #note:  at this link: https://databoys.github.io/Feedforward/
						 #It actually does an activation function:  sigmoid(x) = 1/(1 + np.exp(-x))  --> the np.exp is the e function to the left.
						 #and activation derivative = sigmoid(y) - (1 - sigmoid(y))

	#straight from:  https://databoys.github.io/Feedforward/
	#also from: https://databoys.github.io/Feedforward/
	#Using one function for both feedforward and backprop was inspired by Siraj Raval videos (thanks Siraj!)
	def sigmoid(x, derivative):
		sigmoid = 1 / (1 + np.exp(-x))
		if (derivative == True):
			return sigmoid * (1.0 - sigmoid)
		return sigmoid

	#Rectified Linear Unit activation function.
	#It outputs zero as long as x is zero, and outputs x when x is >= 0.
	#What the heck is the derivative of this thing?  Maybe I won't use it yet.
	def reluActivationFunction(x):
		return numpy.maximum(x, 0)

	#This method will create a new network and train it - something to couple training examples with their proper output.
	#I've already gotten the images arranged in folders by classes - the class comes from the Google image search term.
	#So whatever the folder name is, that should be the expected output.  However many folders I have, I should have that many neurons in the
	#output layer.
	#The training manager then would just grab images at random from the various folders, and in calculating the error, it would expect that neuron
	#representing that folder's class to be 1, and the other neurons to be 0.
def trainToConvergence():
	network = NeuralNetwork()
	network.addLayer(inputLayer)

	for x in range(inputLayer.len, 2, 100):
		network.addLayer(x)

	#Loop until error is under a given threshold or time spent is over a given threshold:
	#2. Run imageConvert.py in order to get an image (or batch) from a random folder.
	#3. Set the expected output to be the output neuron for that folder/class = 1, and all other output neurons 0.
	#4. Move the image into the input layer (imageConvert.py should have it ready to go).
	#5. Forward propagate.
	#6. Calculate error (easy, considering #3).
	#7. Print error.
	#8. Backpropagate.
	#When finished looping, save the weights.

#Once I have a network trained and the weights saved to file, I can grab the weights and do
#classifying on an arbitrary image to see if it matches any of my trained classes:
def runNeuralNetwork(inputLayer):
	#Load the saved weights from file and initialize the network
	#set layers to the data gotten from file.
	network = NeuralNetwork(layers);
	classes = ["dog","cat","monkey","etc"] #need to automate setting these based on input from command line and chromedriver

	network.forwardPropagateNetwork(inputLayer)
	network.printTop5Results()

	#Idea for later:  some kind of metadata analysis on the Google images (file names - or resubmit the image to Google image search and
	#make sure that the file names returned have the same class name)
