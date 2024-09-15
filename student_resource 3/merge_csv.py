import pandas as pd
import os

def merge_csvs(input_folder, output_csv):
    # List all CSV files in the specified folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # List to hold DataFrames
    dataframes = []
    
    # Loop through each CSV file and append the DataFrame to the list
    for file in csv_files:
        file_path = os.path.join(input_folder, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
    
    # Concatenate all DataFrames
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the merged DataFrame to a new CSV
    merged_df.to_csv(output_csv, index=False)
    print(f"Merged CSV saved as {output_csv}")

# Example usage
input_folder = 'csv_folder'  # Folder containing the CSV files
output_csv = 'merged_output.csv'  # Output file name for merged CSV

# Call the function to merge CSV files
merge_csvs(input_folder, output_csv)
