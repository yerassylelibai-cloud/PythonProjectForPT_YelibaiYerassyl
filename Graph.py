from FindMAE import FindMAE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Graph(FindMAE):
    def __init__(self, data):
        super().__init__(data)
    def BuildGraph(self):

        plt.figure(figsize=(8,6))

        plt.scatter(self.clean_x, self.clean_y, color = "blue", label = "Height to weight")

        line_x = self.clean_x
        line_y = self.b + self.a * line_x

        plt.plot(line_x, line_y, color = "red", label = "Regression line")

        plt.xlabel("Height (cm)")
        plt.ylabel("Weight (kg)")
        plt.title("Height to Weight Regression")

        plt.grid(True, alpha = 0.5)


        plt.legend()

        return plt.savefig("result.png")

