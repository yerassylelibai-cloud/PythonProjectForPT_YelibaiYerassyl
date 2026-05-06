import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Organize import *
from FindOSL import *
from Table import *
from FindMAE import *
from Graph import *
from fastapi.responses import FileResponse
from fastapi import FastAPI, UploadFile, File
import io

def main(data):
    print(FindMAE(data).CalculateMAE())
    print(Table(data).BuildTable())

    Graph(data).BuildGraph()




main(np.genfromtxt('externals/body.csv', delimiter=',', skip_header=1))



app = FastAPI()


# @app.post("/analyze")
# async def analyze_data(file: UploadFile = File(...)):
#     # 1. Read the uploaded file into a NumPy array
#     content = await file.read()
#     raw_data = np.genfromtxt(io.BytesIO(content), delimiter=',', skip_header=1)
#
#
#
#     mae_calculator = FindMAE(raw_data)
#     mae_value = mae_calculator.CalculateMAE()
#
#     Graph(raw_data).BuildGraph()
#
#     # 3. Return the JSON (This is the "Output" for Task 14)
#     return {
#         "coefficients": {
#             "slope_a": float(mae_calculator.a),
#             "intercept_b": float(mae_calculator.b)
#         },
#         'metrics': mae_value,
#         'table': Table(raw_data).BuildTable().to_dict(),
#         "status": "Success"
#
#     }
#
# @app.get("/view-graph")
# async def view_graph():
#     return FileResponse("result.png")