import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



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
        a, b = np.linalg.lstsq(A, self.y, rcond=None)[0]
        return [a, b]
    def Table(self):
        self.Table = pd.DataFrame(np.column_stack([self.x, self.y]), columns=['height_cm', 'weight_kg'])
        self.Table['pred_weight'] = self.FindOSL()[0] * self.x + self.FindOSL()[1]
        return self.Table


def main(data):
    HW = HeightWeight(data)
    HW.clean()
    # HW.scatter()
    print(HW.Table())

data1 = np.genfromtxt('source/body.csv', delimiter=',', skip_header=1)
main(data1)