# neu_AI_2018
# For 2018 NEU AI class

## Python 3.6 Environment Setup and Test Program

You will need a computer with at least 4GB of RAM.  Faster CPUs and especially GPUs can help accelerate some of the machine learning algorithms we will be using, so it is recommended that you install Python and work on the fastest machine you have available.  Plan on spending approximately 1 hour to install the software, and 2 hours to complete the Page Rank task.  It is expected that you will interact with the course TA before class begins, if you have any difficulties with the above.
1. It is expected that you will have Python 3.6 running on your machine before the first day of class.
2. It is expected that you will have written some simple Python code to demonstrate it is working before the first day of class.  Your task will be to implement a simple version of Google’s Page Rank algorithm and bring your results to class on the first day.  Further instructions are below.

For Python installation, we highly recommend the use of Anaconda package manager for its simplicity and known success with the packages to be used in our AI class.  Instructions follow:
1.	Download and install Anaconda for Windows/Mac/Linux here:  https://www.anaconda.com/download/
2.	Follow instructions on the Anaconda site to ensure you are running Python 3.6 
(other versions may not be compatible with the machine learning packages we will use) 
Note that it is possible to downgrade (or upgrade) your Python version after you have installed the Anaconda environment and package manager.
3.	Download “python_packages.txt” from here:
 https://github.com/migai/neu_AI_2018
4.	Open a terminal on Mac/Linux, or the special “Anaconda Prompt” command shell in the Windows Start Menu and run the following commands:
conda config --append channels conda-forge
conda config --append channels menpo
conda install --yes --file python_packages.txt
5.	Open the “Anaconda Navigator” and from the “Environments” tab on the left, you can check the proper installation and versions of all the packages and of your Python itself.
From the “Home” tab in Anaconda Navigator, you can open an instance of Jupyter (browser-based Python) or Spyder (a conventional IDE with debug capabilities).
6.	Try running a “hello, world” print program from Jupyter or Spyder to make sure you know how to run Python.  You need just a single line in your program:
print(“hello, world”)
