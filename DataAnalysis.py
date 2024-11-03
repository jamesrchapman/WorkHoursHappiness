import pandas as pd

# Define column widths based on spacing (modify as needed)
colspecs = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25)]  # Adjust these based on actual spacing

# Load the .dat file
df = pd.read_fwf('your_file.dat', colspecs=colspecs, header=None)

# Rename columns based on structure
df.columns = ['Var1', 'Var2', 'Var3', 'Year', 'ID']

# Display the first few rows to inspect
print(df.head())