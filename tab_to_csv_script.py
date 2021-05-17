import csv
import pandas

dataframe = pandas.read_csv("usgs_paria_2020.txt",delimiter="\t")
dataframe.to_csv("NewProcessedDoc.csv", encoding='utf-8', index=False)
