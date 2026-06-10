import pandas as pd

data = pd.read_csv(
    r"C:\Users\AKSHAT\OneDrive\Documents\Placement Project\dataset\placement_project.csv"
)

print("Columns:")
print(data.columns)

print("\nDataset Shape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())