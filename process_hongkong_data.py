import pickle
import numpy as np
import pandas as pd
import sys

with open('./input_Hong_Kong/hongkong_processed_order_11_29.pickle', 'rb') as f:
    original_dict = pickle.load(f)

# Create a new dictionary to store the reformatted data
new_dict = {}

# Initialize variables to keep track of the current day and order count
current_day = 0

for key, value in sorted(original_dict.items()):
    day_index = int(key / 86400) + 1
    adjusted_key = key - ((day_index - 1) * 86400)
    
    # The 8th item in value should also be updated to be equal to 0-86400 based key
    if day_index != current_day:
        current_day = day_index
        # value[0][8] = adjusted_key
        new_dict[f'day{current_day}'] = {key: value}
    else:
        # value[0][8] = adjusted_key
        new_dict[f'day{current_day}'].update({key: value})

with open('./input_Hong_Kong/hongkong_date_based_order_test.pickle', 'wb') as f:
    pickle.dump(new_dict, f)