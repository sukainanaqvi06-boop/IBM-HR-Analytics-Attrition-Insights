CREATE DATABASE IF NOT EXISTS hr_attrition_project;

USE hr_attrition_project;
SELECT COUNT(*)FROM hr_data;

-- 1. TOTAL ATTRITION
SELECT count(Attrition)
FROM hr_data
WHERE Attrition = 'Yes';

-- 2. VALUE OF ATTRITION 
SELECT count(Attrition)
FROM hr_data;

-- 3. DEPARTMENT WISE ATTRITION
SELECT Department, count(Attrition) AS department_attrition
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY Department
ORDER BY department_attrition DESC;

-- 4. SALARY WISE ATTRITION
SELECT MonthlyIncome, count(Attrition) AS salary_attrition
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY MonthlyIncome
ORDER BY salary_attrition DESC
LIMIT 5; 

-- 4. GENDER WISE ATTRITION 
SELECT Gender, count(Attrition) AS gender_attrition
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY Gender
ORDER BY gender_attrition DESC;

-- 5. YEAR WISE ATTRITION 
SELECT YearsAtCompany, count(Attrition) AS yearly_attrition
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY YearsAtCompany
ORDER BY yearly_attrition DESC;

-- 6. SATISFACTION WISE ATTRITION
SELECT EnvironmentSatisfaction, count(Attrition) AS satisfaction_attrition
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY EnvironmentSatisfaction
ORDER BY satisfaction_attrition DESC;










