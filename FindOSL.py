import numpy as np
from Organize import *

class FindOSL(OrganizeData):
    def __init__(self, data):
        super().__init__(data)
        self.clean()

    def CalculateOSL(self):
        A = np.column_stack([np.ones(len(self.clean_x)), self.clean_x])
        self.a, self.b = np.linalg.lstsq(A, self.clean_y, rcond=None)[0]