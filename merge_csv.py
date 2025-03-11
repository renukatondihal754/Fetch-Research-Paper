import pandas as pd

# Load both CSV files
output_df = pd.read_csv('output.csv')
pubmed_output_df = pd.read_csv('pubmed_output.csv')

# Merge both DataFrames based on PubmedID, prioritizing non-null fields
merged_df = pd.concat([output_df, pubmed_output_df]).sort_values(by='PubmedID').drop_duplicates(subset='PubmedID', keep='last')

# Save the final merged output
merged_df.to_csv('final_output.csv', index=False)

print("✅ Merging complete. Check 'final_output.csv'")

