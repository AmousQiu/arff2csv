import pandas as pd
import sys
import os

def arff_to_csv(fpath):
    with open(fpath,encoding="utf-8") as file:
        header = []
        for line in file:
            if line.startswith("@attribute"):
                header.append(line.split()[1])
            elif line.startswith("@data"):
                break

        df = pd.read_csv(file,header=None)
        df.columns = header
        filename = fpath[:fpath.find('.arff')]+'.csv'
        df.to_csv("./csv/"+filename,index=None)
        print(filename,"successfully converted!")


all_files = os.listdir("./")
#Check if csv folder already exisits
if not os.path.exists("./csv"):
    os.makedirs("./csv")
    print("CSV Folder created ...")

for file in all_files:
    if file.find('.arff')>=0:
        arff_to_csv(file)

print("Done!")

