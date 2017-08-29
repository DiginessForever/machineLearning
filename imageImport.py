from PIL import Image
import glob, os
import numpy
import random

def removePreviouslyConvertedImages(imagePath):
	imagePath += "/convertedImage*.jpg"
	print("imagePath: " + imagePath)
	myGlob = glob.glob(imagePath)
	for delFile in myGlob:
		os.remove(delFile)
	#throwAwayVar = raw_input("Check now...")

def saveImage(imagePath, img):
	img.save(imagePath)

def resizeImage(imagePath, baseheight):
	img = ''
	try:
		#https://opensource.com/life/15/2/resize-images-python
		img = Image.open(imagePath)
		hpercent = (baseheight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, baseheight), Image.ANTIALIAS)
	except IOError:
		pass
	#print(type(img))
	
	return img #If it failed to open the image, this returns an empty

def saveImage(newImagePath, img):
		print("image path: " + newImagePath)
		try:
			img.save(newImagePath)
		except IOError:
			try:
				img.convert('RGB').save(newImagePath)
			except IOError:
				pass

#https://infohost.nmt.edu/tcc/help/pubs/pil/image-constructors.html
def getImages(imagePath):
	myGlob = glob.glob(imagePath + "/*.jpg")
	myList = []

	baseheight = 480
	count = 0
	for infile in myGlob:
		img = resizeImage(infile, baseheight)
		if (img != ''):
			#img.save(imagePath + "/convertedImage" + str(count) + ".jpg")
			newImagePath = imagePath + "/convertedImage" + str(count) + ".jpg"
			saveImage(newImagePath, img)
			myList.append(numpy.asarray(img).flatten(order='C'))
			count += 1

	count = 0
	for image in myList:
		count += 1
		print("convertedImage" + str(count) + " length: " + str(image.size) + ", array shape: " + str(image.shape))

	return myList  #This has a bunch of elements, each of which is a picture...

def getMaxSize(myList):
	maxSize = 0
	for image in myList:
		if image.size > maxSize:
			maxSize = image.size
	return maxSize


#I'm still getting the error:
#TypeError: only integer scalar arrays can be converted to a scalar index
#I must not understand numpy arrays (ndarrays) well enough yet.
def createBatch(myList, batchSize):
	#In dropout, they select 50% usually from the total.
	#Basically, if you train with random pictures from the list each time, you get this
	#strengthening effect.
	#Also, convert from 0-255 to 0-1.
	#totalImagesToGrab = int(len(flattenedList) * (percentToSelect / 100))
	oneDimensionalBatch = numpy.empty([1],dtype=float)

	count = 0
	while batchSize > 0:
		indexToGrab = random.randrange(0, len(myList) - 1)
		for pixelIndex in range(0, len(myList[indexToGrab]) -1):
			#pixel = float(pixel)
			pixel = myList[indexToGrab][pixelIndex] / 255.0
			myList[indexToGrab][pixelIndex] = pixel

		a = numpy.asarray(myList[indexToGrab][0:len(myList[indexToGrab])], dtype=float)
		oneDimensionalBatch = numpy.concatenate([oneDimensionalBatch, a])
		count += 1
		print(str(count)+".oneDimensionalBatch size: " + str(oneDimensionalBatch.size))
		batchSize -= 1

	return oneDimensionalBatch

def main():
	from sys import argv #This grabs any arguments passed through the command line
	#print(argv)
	if (len(argv) > 1):
		imagePath = argv[1]
	else:
		imagePath = "*.jpg"  #This assumes we are running this script in a folder with .jpg formatted images in it.
	removePreviouslyConvertedImages(imagePath)
	myList = getImages(imagePath)
	maxSize = getMaxSize(myList)
	print("maxSize: " + str(maxSize))

	myBatch = createBatch(myList, 50) 	#Get a batch of 50 pictures
	print("batch length: " + str(myBatch.size))

if __name__ == "__main__":
	main()