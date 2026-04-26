import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Organize import *
from FindOSL import *
from Table import *
from FindMAE import *
from Graph import *

def main(data):
    print(FindMAE(data).BuildTable())
    Graph(data).BuildGraph()




main(np.genfromtxt('externals/body.csv', delimiter=',', skip_header=1))
