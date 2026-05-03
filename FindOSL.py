import numpy as np
from Organize import *

class FindOSL(OrganizeData):
    def __init__(self, data):
        super().__init__(data)
        self.clean()

    def CalculateOSL(self):
        A = np.column_stack([np.ones(len(self.clean_x)), self.clean_x])
        self.b, self.a = np.linalg.lstsq(A, self.clean_y)[0]
