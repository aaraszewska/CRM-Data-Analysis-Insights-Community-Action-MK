import pandas as pd

file_path = "data/Organisations-260327090500.xlsx"  

df = pd.read_excel(file_path)

print("=== HEAD ===")
print(df.head())

print("\n=== COLUMNS ===")
print(df.columns)

print("\n=== INFO ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# liczba organizacji
print("Total organisations:", df.shape[0])

# ile ma email
print("\nHas email:")
print(df['Email'].notnull().sum())

# ile ma website
print("\nHas website:")
print(df['Website'].notnull().sum())

# sektor
print("\nSector distribution:")
print(df['Sector'].value_counts().head(10))

# % braków
missing_percent = df.isnull().mean() * 100
print(missing_percent.sort_values(ascending=False).head(10))