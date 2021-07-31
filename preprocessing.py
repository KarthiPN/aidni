import pandas as pd
import numpy as np


# Function to chek NAN and Infinite values in the dataframe.

def data_preprocessing(data):

  if (data.isnull().values.any() == True):
    print("NaN values Identified in your dataset")
    data.fillna(0, inplace=True)
    if (data.isnull().values.any() == True):
      print("couldn't Remove NaN values from the daset")
    else:
      print("Nan fields are removed from the dataset")
  else:
    print("No NaN fields in the dataframe")

  
  if (data.isin([np.inf, -np.inf]).values.any() == True):
    print("infinite values are identified in your dataset")
    data.replace([np.inf, -np.inf], 0, inplace = True)
    if (data.isin([np.inf, -np.inf]).values.any() == True):
      print("Couldn't remove infinite data")
    else:
      print("Infinite data are replaced with 0")
  else:
    print('Infinite data feields not found')


data_preprocessing(df_normal_bin_small)