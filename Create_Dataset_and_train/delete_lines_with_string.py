import pandas as pd
print("start")
# Load the CSV file
folder_name="all_without_ours_3"
file_path = f'../Create_Dataset_and_train/{folder_name}/mfcc_labels_{folder_name}.csv'
df = pd.read_csv(file_path)

# Filter out rows that contain 'wind_data'
# df_filtered = df[~df.apply(lambda row: row.astype(str).str.contains('signal_pitch-shifted.csv').any(), axis=1)]
df_filtered = df[~df.apply(lambda row: row.astype(str).str.contains(r'\\ours_3').any(), axis=1)]

# Save the filtered DataFrame back to the same CSV file
df_filtered.to_csv(file_path, index=False)

print("Lines  have been removed.")
