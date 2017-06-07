#imports here:  numpy, os, whatever I need

n = 1000
e = (1.0 + 1.0/n)^n

#Instantiate a new layer with the number of neurons desired, give the neurons (Q: do neurons have separate values than their weights?) random values.
def layerFactory(numberOfNeurons):


#create weights between layers (essentially, populate the first layer's weight matrix)
def connectLayers(layer1, layer2):


#I don't think I'll have a network factory this time right away - there are too many variables.  I will have a network object, but it'll just have
#a list of layers.
#I need the network class here.