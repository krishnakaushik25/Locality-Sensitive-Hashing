
# convert list to integers
def list_to_integers(features,list_cols,data):
  for c in features:
    if c not in list_cols:
      data[c] = data[c].apply(lambda x: x[0] if type(x) == list else None)
  return data

# remove rows having number of elements above certain threshold for list columns
def remove_rows(list_cols,data):
    for c in list_cols:
        data["count"] = data[c].apply(lambda x: len(x) if type(x) == list else 0)
        data = data[data["count"] <= 16] # here 16 is the thershold value
        data.drop("count", axis=1, inplace=True)
    return data

# sort the values in the list columns replace empty values with empty list
def empty_values(list_cols, data):
    for c in list_cols:
        data[c] = data[c].apply(lambda x: sorted(x) if type(x) == list else [])
    return data

