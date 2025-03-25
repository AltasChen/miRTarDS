import pandas as pd

df = pd.read_csv('miRTarDS_combined.txt', sep='\t')

filtered_df = df[df['miRTarDS Prediction'] == 'Protein-level Interaction']

filtered_df.to_csv('proteinLevel_MTI.txt', sep='\t', index=False)