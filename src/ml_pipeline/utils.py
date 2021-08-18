import numpy as np
import pandas as pd
from itertools import chain
from collections import Counter
from yaml import CLoader as Loader, load

# Function to read the csv file
def read_data_csv(file_path, **kwargs):
    raw_data_csv = pd.read_csv(file_path  ,**kwargs)
    return raw_data_csv

# Function to read the json file 
def read_data_json(file_path, **kwargs):
    raw_data_json = pd.read_json(file_path  ,**kwargs)
    return raw_data_json

#  Function for reading config file
def read_config(path):
    with open(path) as stream:
        config = load(stream,Loader=Loader)
    return config

# Finding the feature importance i.e ranking the users
def feat_imp(p,q):
    """
    Function to calculate feature importance given
    seed set probability of a feature and global
    probability for the same feature
    """
    return (p-q) * np.log((p*(1-q))/((1-p)*q))

# Calculate the features counts in the dataset
def count_fn(data, features, list_cols):
    """
    Function to calculate the features counts in the dataset
    :param data: Dataframe containing user records
    :param features: List of columns in the dataset
    :param list_cols: Columns that can have multiple values per user
    :return: Dataframe with feature count values
    """
    count_df = pd.DataFrame(columns=["value", "count", "feature"])
    for col in features:
        if col not in list_cols:
            counts = data[col].value_counts()
        else:
            counts = pd.Series(Counter(chain.from_iterable(x for x in data[col])))
        counts = counts.reset_index()
        counts.columns = ["value", "count"]
        counts["feature"] = col
        count_df = pd.concat([count_df, counts])
    count_df["sum"] = count_df.groupby("feature")["count"].transform(sum)
    count_df["prob"] = count_df["count"] / count_df["sum"]
    count_df = count_df[["feature", "value", "prob"]]
    return count_df

# Convert column values into string
def conv_values(v, c, list_c):
    """
    Convert column values into string with the column name
    as prefix
    :param v: Feature value
    :param c: Column name
    :param list_c: Boolean, True if c is a list column False otherwise
    :return:
    """
    if list_c:
        final_v = []
        for v_ in v:
            final_v.append(f"{c}_{str(v_)}")
    else:
        final_v = f"{c}_{str(v)}"
    return final_v

# Flatten a list of lists
def flatten_list(f):
    """
    Function to flatten a list of lists
    """
    f_l = []
    for f_ in f:
        if isinstance(f_, list):
            f_l.extend(f_)
        else:
            f_l.append(f_)
    return f_l
