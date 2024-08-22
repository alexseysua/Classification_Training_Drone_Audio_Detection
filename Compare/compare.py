import pandas as pd

# List of CSV file paths
csv_file_paths = [
    '/mnt/data/classification_report_1.csv',
    '/mnt/data/classification_report_2.csv',
    '/mnt/data/classification_report_3.csv',
    # Add more paths as needed
]

# Initialize an empty DataFrame to hold all the data
combined_df = pd.DataFrame()

# Load each file, add a suffix, and concatenate them
for i, file_path in enumerate(csv_file_paths, start=1):
    df = pd.read_csv(file_path)
    # Add suffix to distinguish between models
    df = df.add_suffix(f'_{i}')
    # Combine the data into a single DataFrame
    if combined_df.empty:
        combined_df = df
    else:
        combined_df = pd.concat([combined_df, df], axis=1)

# Assuming the primary comparison metric is 'test_accuracy', find the best model
# Extract just the 'test_accuracy' columns to compare
accuracy_columns = [col for col in combined_df.columns if 'test_accuracy' in col]
best_accuracy = combined_df[accuracy_columns].max(axis=1)
best_model_idx = best_accuracy.idxmax()

# Get the best model's details
best_model = combined_df.loc[best_model_idx]

# Output the best model's details
print("Best Model Based on Test Accuracy:")
print(best_model)

# If you want to save the best model's details to a file, uncomment the following:
# best_model.to_csv('/mnt/data/best_model.csv', index=False)

# Additional visualization or analysis can be performed here