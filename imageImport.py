#import Image
from PIL import Image
import glob, os
import numpy
import pickle

#This is where we convert pixels (values that are in the range of 0-255) to the range of 0-1 (double).
def convertPixelsToNeuronValues(myList):
	myList2 = []
	for pixel in myList:
		myList2.append(pixel / 255)
	return myList2

#In order to make batches out of a list of flattened images, I need to get a random bunch of images from it.
def createBatchFromFlattenedImageList(flattenedList, percentToSelect):
	#I think that in dropout, they select 50% usually from the total.
	#I could get a random picture from the list each time at the risk of repeating pictures.  I think I'll go with that.
	totalImagesToGrab = int(len(flattenedList) * (percentToSelect / 100))

	oneDimensionalBatch = []

	while totalImagesToGrab > 0:
		indexToGrab = random.randrange(0, flattenedList.len - 1)
		numpy.concatenate(oneDimensionalBatch, flattenedList[indexToGrab])
		totalImagesToGrab -= 1

	return oneDimensionalBatch


#Now I have a list of image objects.
#I need to loop through them one at a time and get the pixel data out from each one, then flatten it.
#This method just puts the image data into an ndarray - I don't think it's flattened yet...I still need to do that.
def flattenMyImages(myList):
	myList2 = []
	for image in myList:
		a = numpy.array(image)  #Accepted answer for how to convert image data to a numpy array (ndarray) 
								#from: http://stackoverflow.com/questions/384759/pil-and-numpy
		myList2.append(a.flatten()) #https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html					
	return myList2

#I need to leave enough space in memory to do the neural net stuff.  I have 16GB (roughly 16,000,000,000 bits) of memory.  Should be enough.
#I do not want a lot of intermediate states though, so I'm going straight from the image list to a list of flattened ndarrays.
#I will ultimately make a batch out of these flattened arrays by sticking them end to end.
#Then on to the neural net stuff using Tensorflow.  Should be a simple matter of repeatedly sticking random batches into the input layer,
#doing feedforward & backpropagation, and leaving it running all night, next day...maybe a week or two.  At 9.2 Tflops, I'm sure it'll be as well
#trained as it's going to really get at that point.

#To Do:  
#1.  Create the neural net
#	a.  Create the input layer.
#	b.  Create a dropout layer (I wonder if these could be the same - I could actually just do dropout myself - step #4 above)
#	c.  Pooling layer (cover that again)
#	d.  Fully connected layers (3)
#	e.  Output layer

#2.  Convert output layer to something that makes sense.
#	a.  If I have two classes, the output layer should have two neurons.
#	b.  Each neuron should correspond to a class.
#	c.  The output function should display each class's probability.


#https://infohost.nmt.edu/tcc/help/pubs/pil/image-constructors.html
def getImageObjectArrayOfFolderImages(queryString):
	queryString += "/*.jpg"
	myGlob = glob.glob(queryString)
	myList = []

	for infile in myGlob:
		try:
			myList.append(Image.open(infile))
		except IOError:
			pass

	#myFile = open("import1_createImageArray.log",'w')
	#for item in myList:
	#	myFile.write("%s\n" % item)   #This method just writes a small text description of the file
	#pickle.dump(myList, myFile) #maybe I'll get more data this way

	return myList  #This has a bunch of elements, each of which is a picture...

#query string being something like "*.jpg" (if all the images are jpeg files with .jpg extension)
def getLargestImageFileSizeInFolder(myList):
	maxX = 0
	maxY = 0
	maxSize = [0,0]

	for image in myList:
		if (image.size[0] > maxX):
			maxX = image.size[0]
		if (image.size[1] > maxY):
			maxY = image.size[1]

	maxSize[0] = maxX
	maxSize[1] = maxY

	return maxSize


#Return the total pixels of a given image size (x * y)
def getTotalPixels(size):
	return size[0] * size[1] #Not sure if this is exactly right - another search required

#https://docs.python.org/3/tutorial/datastructures.html
def padAllImagesToSize(myList, maxSize):
	newList = []
	for image in myList:
		newList.append(padImageSize(image, maxSize))
	return newList


def padImageSize(image, newSize):
	newImage = Image.new("RGB", newSize)   ## luckily, this is already black!
	newImage.paste(image, ((newSize[0]-image.size[0])/2,
	                  (newSize[1]-image.size[1])/2))
	return newImage


#This is a kind of neat function if I want to reduce the size of an image.
#It loses detail of course.
#Probably a good way to downsize if needed.
def createImageThumbnail(path, size):
	image = Image.open(path)
	return image.thumbnail(size)

#Get largest file size first.  We will then pad the rest of them so that they are all the same size.
#1.  Get all the image paths.
#1.  Get the largest image size.
#2.  Pad all the images to equal that largest size.
#3.  Flatten the images.  http://stackoverflow.com/questions/7762948/how-to-convert-an-rgb-image-to-numpy-array
#						http://stackoverflow.com/questions/384759/pil-and-numpy
#						Is this slower?  Another way:  http://stackoverflow.com/questions/13550376/pil-image-to-array-numpy-array-to-array-python
#						Going to have to time the above methods and use the fastest.
#4.  Get a random selection of the flattened images from the total.
#5.  Create a batch (do we string them all together?).
#6.  Put the batch in the input layer of the neural net.
def main():
	from sys import argv #This grabs any arguments passed through the command line
	#print(argv)
	if (len(argv) > 1):
		queryString = argv[1]
	else:
		queryString = "*.jpg"  #This assumes we are running this script in a folder with .jpg formatted images in it.
	myList = getImageObjectArrayOfFolderImages(queryString)
	maxSize = getLargestImageFileSizeInFolder(myList)
	print("maxSize: " + str(maxSize))
	for picture in myList:
		print(picture)
	#myList = padAllImagesToSize(myList, maxSize)
	#myList = flattenMyImages(myList)
	#myList = createBatchFromFlattenedImageList(myList, 50) 	#Get a total of 50% of the flattened images, put them end to end (extra flattened) in another
														#Ndarray.  This is considered a batch and will go onto the input layer of the neural net after
														#the pixel values are adjusted to be between 0 and 1.
													   	#(some may be repeated, in which case less than half of the unique images will be selected)
	#myList = convertPixelsToNeuronValues(myList) #This is where we convert pixels (values that are in the range of 0-255) to the range of 0-1 (double).
	#print(myList)

if __name__ == "__main__":
	main()