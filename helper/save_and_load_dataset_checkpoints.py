import json
import pickle

# Use the below functions to save/load your list of dictionaries as JSON
# 
# Examples:
#   - save_data("disney_data_cleaned.json", movie_info_list)
#   - movie_info_list = load_data("disney_data_cleaned.json")

def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(title):
    with open(title, encoding="utf-8") as f:
        return json.load(f)

# Use the below functions to save/load your list of dictionaries as PICKLE file
#
# Examples: 
#   - save_data_pickle("disney_movie_data_cleaned_more.pickle", movie_info_list)
#   - a = load_data_pickle("disney_movie_data_cleaned_more.pickle")

def save_data_pickle(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f)

def load_data_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)