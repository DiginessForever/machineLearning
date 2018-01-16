Explanation of files:

chromedriver.py:  
	Description:  Python script which uses Selenium chromedriver to download images from Google images automatically.
	
	Usage:  "python chromedriver.py <search term here>" ie - "python chromedriver.py cat".
	
	What will happen:  It will open up an instance of the Chrome browser, automatically navigate to Google Images,
		enter "cat", wait for images to pop up, scroll until it cannot anymore, then download all the images into the same
			folder.
			
	Dependency:  Selenium's "chromedriver" binary - needs to be in the same folder as this python script.

imageImport.py:
	Description:  use command "python imageImport.py <relative folder path to images>" 
	              example: "python imageImport.py images/car
	
	What it will do:  
	1.  Go down from the folder the script is in, into the subfolder images, then subfolder car,
	then it will load all the images that are readable (ignoring corrupted images or unrecognized formats) into a list.
	2.  Convert the images into a standard height, with varying width to keep the aspect ratio, and save the
	converted images into the same folder with names: "convertImageX.jpg" where X is the sequence number of the image.
	3.  Save the converted version of the images in a list in memory with each image element of the list
	converted into an ndarray of pixel values.
	4.  Finally, it will create batches of images for input to the neural net, converting the pixel value ranges from
	0-255 to 0-1.
	

pythonReluNeuralNet.py:
	Description:  Work in progress.  I am converting my Javascript ANN to Python.  In the process, I am exploring using
		Numpy matrices instead of double for loops, and using the Relu activation function instead of a sinusoidal one.
		
	Usage:  I cannot use this until I am finished.
	
	Action needed:  
		Fully get the matrix multiplications working for the feed forward method
		Refresh my memory on backpropagation
		Recode the backprop
		Get the data flowing into the input layer from "import Image.py"
		Start testing the training process using:
			chromedriver.py
			import Image.py
			pythonReluNeuralNet.py
		Once I get minimally acceptable results, start moving to CUDA or do more comparisons with Tensorflow layers/objects

tensorStarter.py:
	empty placeholder file - will use this if I start using Tensorflow instead of my own neural net (can use both CPU and GPU)

init.py:
	This file is required by Python's interpretor in order to allow importing Python scripts (typically have filenames ending in .py) from this folder into other Python scripts.  It would be empty, but Github has a requirement that files have content in order to be committed.  I added a single '.' to the file for this reason.
	
------------------------------------------
Intent:
The final product of this repo should be a tool usable with a single command:
Once I get the training manager written, you should be able to give a command like this:  "python training_manager cat dog car wheel ..." (the ... represent a bunch of names of object types)
It will automatically cycle through each object type, downloading all the images for each and saving them in folders.  Then it will run image import on each individually.  Then it will instantiate a neural net, train the net to recognize that object type, and save the weight matrix (trained memory of the neural net).

At that point, I'll be pretty happy, but will still need to continue optimizing, as well as thinking about how to train for the image types together (I'll have to randomize the folder it pulls the image from, while appropriately setting the expected output layer according to the folder name the image came from).

The next stage will be getting the training manager to monitor the recognition rate and try mitigating strategies when the network will not converge on specific classes.

If you use this, let me know how it went and what you liked or didn't: diginess@gmail.com
