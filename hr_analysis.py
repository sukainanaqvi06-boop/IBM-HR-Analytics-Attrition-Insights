import pandas as pd

df = pd.read_csv("HR-Employee-Attrition.csv")
print(df.shape)
print(df.head())
print(df.columns)

# 1. check missing values
print("Missing Values")
print(df.isnull().sum())

# 2. check for duplicates
print("\nDuplicate Values")
print(df.duplicated().sum())

# 3. check data types
print("\nData Types")
print(df.dtypes)

edu_col_change = ["Education", 'EnvironmentSatisfaction', 'JobSatisfaction',]

df[edu_col_change] = df[edu_col_change].astype(object)
print(df.dtypes)
print("Cleaned Data")

# 4. value of attrition
value_attrition = df["Attrition"].value_counts()
print("\nvalue of attrition")
print(value_attrition)

attrition_df = df[df["Attrition"] == "Yes"]

# 5. Department wise attrition
department_attrition = attrition_df.groupby("Department")['Attrition'].count().sort_values(ascending=False)
print("\ndepartment_wise_attrition")
print(department_attrition)

# 6. salary wise attrition
salary_attrition = attrition_df.groupby('MonthlyIncome')['Attrition'].count().sort_values(ascending=False)
print("\nsalary wise attrition")
print(salary_attrition)

# 7. gender wise attrition
gender_attrition = attrition_df.groupby('Gender')['Attrition'].count().sort_values(ascending=False)
print("\ngender wise attrition")
print(gender_attrition)

# 8. year wise attrition
yearly_attrition = attrition_df.groupby('YearsAtCompany')['Attrition'].count().sort_values(ascending=False)
print("\nyear wise attrition")
print(yearly_attrition)

# 9. satisfaction wise attrition
satisfaction_attrition = attrition_df.groupby('EnvironmentSatisfaction')['Attrition'].count().sort_values(ascending=False)
print("\nsatisfaction_attrition")
print(satisfaction_attrition)

df.to_csv("clean_hr.csv", index=False, encoding='utf-8-sig')
print("clean_csv")

import pandas as pymysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:mysql1332@localhost/hr_attrition_project")

df.to_sql("hr_data", engine, if_exists="replace", index=False)
print("1470 rows MySQL")