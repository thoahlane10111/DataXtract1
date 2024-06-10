import pandas as pd

def extract_data_from_excel(excel_file_path):
    # Read Excel file into pandas DataFrame
    df = pd.read_excel(excel_file_path)
    # Perform data cleaning and preprocessing if needed
    return df
