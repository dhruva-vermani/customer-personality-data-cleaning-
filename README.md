# customer-personality-data-cleaning-
Data cleaning using pandas

# Data Cleaning and Preprocessing – Customer Personality Analysis (https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

## Objective

The objective of this project was to clean and preprocess a raw dataset by identifying and handling missing values, removing duplicate records, standardizing categorical data, converting date formats, and verifying data types to prepare the dataset for further analysis.

## Dataset

Customer Personality Analysis Dataset

## Tools Used

* Python
* Pandas

## Data Cleaning Steps Performed

### 1. Missing Value Treatment

* Identified missing values using `isnull().sum()`.
* Found missing values in the `income` column.
* Replaced missing income values with the median income to preserve data integrity without removing records.

### 2. Duplicate Record Handling

* Checked for duplicate rows using `duplicated().sum()`.
* No duplicates found
  
### 3. Standardization of Categorical Data

#### Marital Status

The original dataset contained multiple marital status categories such as:

* Single
* Married
* Together
* Divorced
* Widow
* Alone
* YOLO
* Absurd

These were consolidated into three meaningful categories:

* Single
* Married
* Divorced

#### Education

Education levels were grouped into broader categories:

* Basic → School
* 2n Cycle → School
* Graduation → Graduate
* Master → Postgraduate
* PhD → Postgraduate

This improved consistency and simplified analysis.

### 4. Column Name Standardization

* Converted column names to lowercase.
* Removed inconsistencies in naming conventions.


Examples:

* `Year_Birth` → `year_birth`
* `Marital_Status` → `marital_status`
* `Dt_Customer` → `dt_customer`

### 5. Date Format Conversion

* Converted the `dt_customer` column from string format to datetime format using `pd.to_datetime()`.
* Ensured consistent date representation throughout the dataset.

### 6. Data Type Validation

Verified that:

* Numerical columns were stored as `int64` or `float64`.
* Categorical columns were stored as strings.
* Date columns were stored as datetime objects.

### 7. Data Quality Verification

After cleaning:

* Missing values were eliminated.
* Duplicate records were removed.
* Categorical values were standardized.
* Date formats were made consistent.
* Data types were validated and corrected where necessary.

## Output

The cleaned dataset was exported as:

`cleaned_marketing_campaign.csv`


