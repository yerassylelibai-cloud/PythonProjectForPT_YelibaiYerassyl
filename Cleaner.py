import numpy as np
import matplotlib.pyplot as plt
from contourpy.util import data


class CleanScatter:
    def __init__(self, data):
        self.x = data[:,0] #height
        self.y = data[:,1] #weight
    def clean(self):
        mask = np.isfinite(self.x) & np.isfinite(self.y)
        self.x = self.x[mask]
        self.y = self.y[mask]
    def scatter(self):
        plt.scatter(self.x, self.y, color='red', label='Data points')
        plt.xlabel('Height (cm)')
        plt.ylabel('Weight (kg)')
        plt.title('Height vs Weight')
        plt.legend()
        return plt.show()

def main(data):
    CS = CleanScatter(data)
    CS.clean()
    CS.scatter()

data1 = np.array([
    [155, 55], [160, 60], [162, 58], [165, 65],
    [168, 70], [170, 68], [172, 75], [175, 80],
    [178, 82], [180, 85], [183, 90], [158, 62],
    [163, 67], [169, 72], [174, 78], [np.nan, 76],
    [176, np.nan],
])  #test
main(data1)