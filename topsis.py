import sys
import pandas as pd
import numpy as np
import os


def topsis(input_file, weights, impacts, output_file):

    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(" Error: Input file not found!")
        sys.exit(1)

  
    if data.shape[1] < 3:
        print(" Error: Input file must contain at least 3 columns!")
        sys.exit(1)

  
    criteria_data = data.iloc[:, 1:]

   
    if not np.issubdtype(criteria_data.dtypes.values[0], np.number):
        print(" Error: Criteria columns must contain numeric values only!")
        sys.exit(1)

    for col in criteria_data.columns:
        if not pd.api.types.is_numeric_dtype(criteria_data[col]):
            print(" Error: All criteria columns must be numeric!")
            sys.exit(1)

  
    weights = weights.split(",")
    impacts = impacts.split(",")

   
    if len(weights) != criteria_data.shape[1]:
        print(" Error: Number of weights must match number of criteria columns!")
        sys.exit(1)

    if len(impacts) != criteria_data.shape[1]:
        print(" Error: Number of impacts must match number of criteria columns!")
        sys.exit(1)

   
    for imp in impacts:
        if imp not in ["+", "-"]:
            print(" Error: Impacts must be either '+' or '-' only!")
            sys.exit(1)

    
    weights = np.array(weights, dtype=float)


    norm_matrix = criteria_data / np.sqrt((criteria_data ** 2).sum())

   
    weighted_matrix = norm_matrix * weights

    
    ideal_best = []
    ideal_worst = []

    for i in range(criteria_data.shape[1]):
        if impacts[i] == "+":
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

  
    score = dist_worst / (dist_best + dist_worst)

   
    rank = score.rank(ascending=False)

   
    data["Topsis Score"] = score
    data["Rank"] = rank.astype(int)

    
    data.to_csv(output_file, index=False)

    print(" TOPSIS Successfully Completed!")
    print("Output Saved in:", output_file)



if __name__ == "__main__":

   
    if len(sys.argv) != 5:
        print(" Error: Incorrect number of parameters!")
        print(" Usage:")
        print("python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")
        print(" Example:")
        print('python topsis.py data.csv "1,1,1,2" "+,+,-,+" result.csv')
        sys.exit(1)

   
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
