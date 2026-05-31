import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print(df.head()) #display first 5 rows from the ds
print(df.isnull().sum()) #total cells having null values for every column
print(df[df.isnull().any(axis=1)]) #displays all rows with null values = 24 rows
df['Income'] = df['Income'].fillna(df['Income'].median()) #handle null values , null values = median value
print(df.isnull().sum()) #verifying if null values are handled

print("Duplicate rows:", df.duplicated().sum()) #counts how many duplicate rows exist
#no duplicates found


print(df['Marital_Status'].unique()) #checking  and displaying unique values for marital status
df['Marital_Status'] = df['Marital_Status'].replace({
    'Single': 'Single',
    'Alone': 'Single',
    'YOLO': 'Single',
    'Absurd': 'Single',

    'Married': 'Married',
    'Together': 'Married',

    'Divorced': 'Divorced',
    'Widow': 'Divorced'
})  #Standardizing the values

print(df['Marital_Status'].unique()) #verify

print(df.columns) #print all columns
print(df['Education'].unique())
df['Education'] = df['Education'].replace({
    'Basic': 'School',
    '2n Cycle': 'School',
    'Graduation': 'Graduate',
    'Master': 'Postgraduate',
    'PhD': 'Postgraduate'
})
print(df['Education'].unique()) #verify

df['Dt_Customer'] = pd.to_datetime(
    df['Dt_Customer'],
    dayfirst=True
) #standardize date

df.columns = (
    df.columns
      .str.lower()
      .str.strip()
      .str.replace(' ', '_')
) #rename column name format :column_name(lower case)

#dd-mm-yyyy format


df['dt_customer'] = df['dt_customer'].dt.strftime('%d-%m-%Y')

print(df['dt_customer'].head()) #verify date

#check data types
print(df.dtypes)
#only one data type needs fixing

df['dt_customer'] = pd.to_datetime(
    df['dt_customer'],
    dayfirst=True
)
print(df['dt_customer'].dtype)
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print(df.isnull().sum())
