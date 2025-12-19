import pickle
import pandas as pd

# REPLACE with your actual filename
MODEL_FILE = 'rf_model.pkl' 

print(f"--- INSPECTING {MODEL_FILE} ---")

try:
    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)
    
    print(f"\nType of Object: {type(model)}")
    
    # Check if it is a list, dictionary, or DataFrame (Common for simple models)
    if isinstance(model, pd.DataFrame):
        print("It is a DataFrame.")
        print(model.head())
    elif isinstance(model, dict):
        print(f"It is a Dictionary with keys: {list(model.keys())[:5]}")
    else:
        # It is likely a Scikit-Learn or Surprise object
        print(f"\nMethods available: {[x for x in dir(model) if not x.startswith('__')]}")
        
except Exception as e:
    print(f"Error loading pickle: {e}")

# Add this at the bottom
if hasattr(model, 'n_features_in_'):
    print(f"\nThis model expects {model.n_features_in_} columns of data.")
    if hasattr(model, 'feature_names_in_'):
        print(f"Examples of columns needed: {model.feature_names_in_[:10]}")