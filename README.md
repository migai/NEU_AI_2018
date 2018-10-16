![AI Logo](https://github.com/migai/NEU_AI_2018/blob/master/utils/2018_NEU_AI_Banner.jpg "AI Logo") 
## Computer Setup and Pre-Class Assignment

We will be running packages in the Python 3.6 (or higher) environment.  You will need a computer with at least 4GB of RAM.  Faster CPUs and especially GPUs can help accelerate some of the machine learning algorithms we will be using, so it is recommended that you install Python and work on the fastest machine you have available.  *If you have any difficulties with the following two tasks, it is expected that you will interact with the course TA **before** the first day of class.*

:exclamation:1. *It is expected that you will have Python 3.6 or 3.7 running on your machine before the first day of class.*  (1 hour)

:exclamation:2. *It is expected that you will have executed some simple Python code to demonstrate it is working before the first day of class.*  Your task will be to implement a simple version of Google’s PageRank algorithm and **bring your results to class on the first day**.  Further instructions will be provided to help you. (1 to 3 hours, depending on your familiarity with Python)

## Python 3 Installation
For Python installation, we highly recommend the use of the **Anaconda** package manager for its simplicity and known success with the packages to be used in our AI class.  You can use alternative installations of Python if you do not like Anaconda, but you may need to work with the course TA to ensure all associated packages are properly installed (see *python_packages.txt* from [https://github.com/migai/NEU_AI_2018]), and you will need to ensure you are using Python version 3.6 or higher.
Instructions for **Anaconda** clean install are here:

### 1. Install the **Anaconda** Package Manager
Download and install Anaconda for Windows/Mac/Linux here:  [https://www.anaconda.com/download/]

Follow instructions from the Anaconda download site to ensure you are running **Python 3.6.x** or **Python 3.7.x**
(Earlier versions of Python may not work properly when assignments are being graded.) 


### 2. Verify You are Using Python 3.6.x or 3.7.x
*Make sure you are using Python 3.6.x **before** you continue with the following steps.*
*Open a terminal on Mac/Linux, or use the special “Anaconda Prompt” command shell in the Windows Start Menu.

### 3. Install Python Packages for the AI Course
  *Download **python_packages.txt** from here: [https://github.com/migai/NEU_AI_2018]
  
  *Open a terminal on Mac/Linux, or use the special “Anaconda Prompt” command shell in the Windows Start Menu.
  
  Run the following commands, adjusting to your **conda** path or the .txt file path as necessary:
  ```bash
  conda config --append channels conda-forge
  conda config --append channels menpo
  conda install --yes --file python_packages.txt
  ```
      
### 4. Check Your Package Installation with **Anaconda Navigator**
Open the **Anaconda Navigator** executable you just installed.  On the left, you can select "Environments" to check the proper installation and versions of all the packages.  Be sure your Python is a version of 3.6 and not 3.7!

### 5. Open a Python IDE
By selecting “Home” from the left side of **Anaconda Navigator**, you should be able to open an instance of Jupyter (browser-based Python) or Spyder (a conventional IDE with debug capabilities).  Either one is fine for your work in this course.  Jupyter will allow you to better describe your programs to the graders, but Spyder can be more flexible and familiar to you.

### 6. Check that You Can Run Python
Try running a *“hello, world”* print program from your preferred environment (Jupyter or Spyder, for example) to make sure you can run Python.  You need just a single line in your program:
```python
print(“hello, world”)
```
:checkered_flag:
