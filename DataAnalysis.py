import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


# Define column widths based on spacing (modify as needed)
colspecs = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25)]  # Adjust these based on actual spacing

# Load the .dat file
df = pd.read_fwf('GSS.dat', colspecs=colspecs, header=None)

# Rename columns based on structure
df.columns = ['Ballot', 'WorkHours', 'happiness', 'Year', 'ID']

# Display the first few rows to inspect
print(df.head())


df_filtered = df[df['WorkHours'] > -1]
df_filtered = df_filtered[df_filtered['happiness'] > 0]

print(df_filtered.head())


# Basic descriptive statistics for work hours and happiness
happiness_by_hours = df_filtered.groupby('WorkHours')['happiness'].mean()
print(happiness_by_hours)

# Correlation between work hours (WorkHours) and happiness (happiness)
correlation = df_filtered['WorkHours'].corr(df_filtered['happiness'])
print("Correlation between work hours and happiness:", correlation)

# Optional: Grouping work hours into categories
df_filtered['WorkHoursCategory'] = pd.cut(df_filtered['WorkHours'], bins=[0, 20, 40, 60, 80], labels=['Low', 'Medium', 'High', 'Very High'])
happiness_by_category = df_filtered.groupby('WorkHoursCategory')['happiness'].mean()
print(happiness_by_category)


# Assuming df_filtered has columns: 'Happiness' (Work Hours) and 'WorkHours' (Happiness)
work_hours_by_happiness = df_filtered.groupby('happiness')['WorkHours'].mean()
print(work_hours_by_happiness)



# Define the ordinal logistic regression model
model = smf.mnlogit('happiness ~ WorkHours', data=df_filtered)

# Fit the model
result = model.fit()

# Display the summary of the model
print(result.summary())