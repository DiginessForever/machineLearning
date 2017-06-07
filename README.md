Explanation of files:

chromedriver.py:  
	Description:  Python script which uses Selenium chromedriver to download images from Google images automatically.
	Usage:  "python chromedriver.py <search term here>" ie - "python chromedriver.py cat".
	What will happen:  It will open up an instance of the Chrome browser, automatically navigate to Google Images,
		enter "cat", wait for images to pop up, scroll until it cannot anymore, then download all the images into the same
			folder.
	Dependency:  Selenium's "chromedriver" binary - needs to be in the same folder as this python script.

goVirtualEnvTensor.sh:
	Description:  A bash script which enters the python virtual environment I have setup for Tensorflow.
	Usage:  "sh goVirtualEnvTensor.sh"
	What will happen:  You'll get a different prompt indicating that the python path has changed and python can only
		execute using that environment's folder's files.
	Possible modification needed:  I need to have it CD to the target directory.

imageConvert.py:
	Description:  A python script which is ran on a folder full of images and does all the processing on them necessary
		to feed them into a neural net.  This is the same file as "import Image.py" except a few hours older.
	Usage:  "python imageConvert.py" - make sure to have a folder full of images and that the folder is properly targeted
		in the python script variable.
	Action needed:  need to get max X or max Y and multiply the two to get the maxImage size.

import Image.py:
	Description:  Same as imageConvert.py, but older (above has more bug fixes)
	Usage:  Same as above.
	Action needed - verify this one is older, verify I have everything, delete this file.

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