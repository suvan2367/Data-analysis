import pandas as pd

df = pd.read_csv("Mall_Customers.csv")	# Loading of dataset

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")	# Clean and standardize headers

df['age'] = df['age'].fillna(df['age'].median())	# Handling of missing values (similar for other columns)

df = df.drop_duplicates()	# Remove duplicate rows, keeping the fist occurence

df['gender'] = df['gender'].str.lower().str.strip()	# Convert to lowercase
df['gender'] = df['gender'].replace({'f': 'Female', 'm': 'Male', 'fem': 'Female', 'mal': 'Male', 'female': 'Female', 'male': 'Male'})	# Standardize the text values

df['doi'] = pd.to_datetime(df['doi'], dayfirst=True, errors='coerce')  
df['doi'] = df['doi'].dt.strftime('%d-%m-%Y')  # Standardize date format dd-mm-yyyy

df['age'] = df['age'].astype('int', errors='ignore')	# Ensure correct data type (similar for other columns)

df.to_csv("cleaned_dataset.csv", index=False)	# Save cleaned dataset

print('first change')