import pandas as pd
from FindOSL import *
from Organize import *

class Table(FindOSL):
    def __init__(self, data):
        super().__init__(data)
        self.CalculateOSL()

    def BuildTable(self):
        self.Table = pd.DataFrame(np.column_stack([self.clean_x, self.clean_y]), columns=['height_cm', 'weight_kg'])
        self.Table['pred_weight'] = self.a * self.clean_x + self.b

        return self.Table