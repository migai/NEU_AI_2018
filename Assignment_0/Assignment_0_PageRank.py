# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 08:38:00 2018
@author: mgaidis
Modified Nov. 17 to fix NetworkX error with some choices of random seed
"""

'''
ASSIGNMENT PART 1:  CHECK PYTHON INSTALLATION
'''

# Start the assignment by checking the installed versions of several
#   python add-on packages that we will use during the AI course.

# First, we will import the packages so we have access to query their
#  version numbers, then we insert code to print out each package's version.
#  Some of the packages will be used in the PageRank assignment, and some will
#  only be used to check on version number.

# The following packages should already be installed by you if you followed
#   instructions for Anaconda installation.  If you do not use Anaconda, you 
#   should install these packages in your python PATH using pip.
import matplotlib      # python's most versatile plotting package
import networkx as nx  # simple, but useful, network/graph package
import nltk            # commonly-used program for processing language
import numpy as np     # very frequently used math and array/matrix package
import pandas          # python's version of Microsoft Excel
import skimage         # scikit-image, useful for machine learning with images
import sklearn         # scikit-learn -- powerful, yet simple machine learning
import scipy           # scientific functions that you might not find in numpy
import statsmodels     # additional statistics functionality
import tqdm            # python utility for timing and function progress

# The pip and sys packages should come pre-installed with your python
import pip             # python package installer
import sys             # sys provides some additional operating system access
print("Path to my active Python executable: " + sys.executable)
print("0. Python version: " + sys.version)

print("1. matplotlib version " + matplotlib.__version__)
print("2. networkx version " + nx.__version__)
print("3. nltk version " + nltk.__version__)
print("4. numpy version " + np.__version__)
print("5. pandas version " + pandas.__version__)
print("6. pip version " + pip.__version__)
print("7. scikit-image version " + skimage.__version__)
print("8. scikit-learn version " + sklearn.__version__)
print("9. scipy version " + scipy.__version__)
print("10. statsmodels version " + statsmodels.__version__)
print("11. tqdm version " + tqdm.__version__)


def make_network(network_nodes, student_id=20161234, n_nodes=5, maxlinks=4):
    """Create a randomized network for PageRank evaluation."""
    
    # We use the student name and ID to create a randomized network for
    #  computing page rank (random so every student's answer will be different)
    network_nodes = network_nodes.upper().replace(" ","")
    if len(network_nodes) < 6:
        network_nodes = network_nodes + "PAGERANK"
    network_nodes = list(set(network_nodes))[:n_nodes]
    node_dict = dict(enumerate(network_nodes))

    import random
    random.seed(student_id)
    n_links = list(range(1,maxlinks+1))
    n_inlinks = random.choices(n_links, k=len(network_nodes))
    n_outlinks = random.sample(n_inlinks, k=len(network_nodes))
    N = nx.generators.degree_seq.directed_havel_hakimi_graph(
        n_inlinks, n_outlinks)
    N = nx.relabel_nodes(N,node_dict)
    nodes = list(N.nodes())
    links = list(N.edges())
    pr = nx.pagerank(N)
    return nodes, links, N, pr



'''
ASSIGNMENT PART 2:  PAGERANK
'''
# 2.1 Create a network graph with nodes labeled with the letters of your name
### ENTER YOUR NAME HERE.  REMOVE MY NAME AND USE YOUR OWN NAME. ###
### IT MUST BE AT LEAST 6 CHARACTERS ###
student_name = "Michael Gaidis"
### ENTER YOUR STUDENT ID HERE ###
student_id = 20164936



# Create the network
try:
    nodes, links, network, pr_nx = make_network(student_name, student_id)
except nx.NetworkXError:
    nodes, links, network, pr_nx = make_network(student_name)
n_nodes = len(nodes)

# Count up the number of outlinks from every node
outlinks = {key: 0 for key in nodes}
for l in links:
    outlinks[l[0]] += 1
    
# Make a dictionary of nodes, listing all inlinks to a given node
inlinks = {key: [] for key in nodes}
for l in links:
    inlinks[l[1]].append(l[0])
    
def within_tolerance(tolerance,pr_old,pr_new):
    return all(abs(pr_new[n] - pr_old[n]) <= tolerance for n in pr_old)

pagerank = {key:0 for key in nodes}
pagerank_new = {key: 1.0/n_nodes for key in nodes}
tolerance = 0.0001
alpha = 0.85
prefactor = (1 - alpha)/n_nodes

while not within_tolerance(tolerance,pagerank,pagerank_new):
    # Update pagerank with another iteration through formula
    pagerank = pagerank_new
    pagerank_new = {key: prefactor for key in nodes}
    for node in pagerank:
        for il in inlinks[node]:
            pagerank_new[node] += (alpha * pagerank[il]/outlinks[il])
          
print("\nNode\tPR-Calc\t\tPR-\u221E")
for n in pagerank_new:
    # see, for example, https://mkaz.blog/code/python-string-format-cookbook/
    print(" {}\t{:.5f}\t\t{:.5f}".format(n,pagerank_new[n],pr_nx[n]))

import matplotlib.pyplot as plt
nx.drawing.nx_pylab.draw_networkx(network, pos=nx.spring_layout(network),
        font_size=14, font_weight='bold', 
        node_size=800, node_color='lightblue',
        edge_color='b', width = 1.5)
plt.axis('off')