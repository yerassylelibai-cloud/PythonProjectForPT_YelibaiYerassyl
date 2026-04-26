import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



class OrganizeData:
    def __init__(self, data):
        self.x = data[:,0] #height
        self.y = data[:,1] #weight

    def clean(self):
        mask = np.isfinite(self.x) & np.isfinite(self.y)
        self.clean_x = self.x[mask]
        self.clean_y = self.y[mask]
