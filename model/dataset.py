import pandas as pd
from sklearn.preprocessing import LabelEncoder

def process_dataset(path):
    """
    Process the dataset and return the processed dataset.
    """
    df = pd.read_csv(path)
    df = df.dropna()
    
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = LabelEncoder().fit_transform(df[column])
    
    return df