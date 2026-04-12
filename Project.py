import numpy as np
import matplotlib.pyplot as plt



class HeightWeight:
    def __init__(self, data):
        self.x = data[:,0] #height
        self.y = data[:,1] #weight
    def clean(self):
        mask = np.isfinite(self.x) & np.isfinite(self.y)
        self.x = self.x[mask]
        self.y = self.y[mask]
    def scatter(self):
        self.clean()
        plt.scatter(self.x, self.y, color='red', label='Data points')
        plt.xlabel('Height (cm)')
        plt.ylabel('Weight (kg)')
        plt.title('Height vs Weight')
        plt.legend()
        return plt.show()
    def FindOSL(self):
        self.clean()
        A = np.column_stack([np.ones(len(self.x)), self.x])
        self.a, self.b = np.linalg.lstsq(A, self.y, rcond=None)[0]



def main(data):
    HW = HeightWeight(data)
    HW.scatter()


data1 = np.genfromtxt('source/body.csv', delimiter=',', skip_header=1)
main(data1)