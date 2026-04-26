from FindOSL import FindOSL
import numpy as np
from Table import Table


class FindMAE(Table):
    def __init__(self, data):
        super().__init__(data)
    def CalculateMAE(self):
        self.mae = float(np.mean(np.abs(self.clean_x-self.BuildTable()["pred_weight"].to_numpy())))
        return {"MAE": self.mae}

