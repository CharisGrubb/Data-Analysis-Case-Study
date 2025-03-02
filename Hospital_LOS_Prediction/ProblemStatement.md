### Objective:
As a Data Scientist, you have been hired by HealthPlus to analyze the data, find out what factors affect the LOS the most, and come up with a machine learning model which can predict the LOS of a patient using the data available during admission and after running a few tests. Also, bring about useful insights and policies from the data, which can help the hospital to improve their health care infrastructure and revenue.

### Data Dictionary:
The data contains various information recorded during the time of admission of the patient. It only contains records of patients who were admitted to the hospital. The detailed data dictionary is given below:

- patientid: Patient ID
- Age: Range of age of the patient
- gender: Gender of the patient
- Type of Admission: Trauma, emergency or urgent
- Severity of Illness: Extreme, moderate, or minor
- health_conditions: Any previous health conditions suffered by the patient
- Visitors with Patient: The number of patients who accompany the patient
- Insurance: Does the patient have health insurance or not?
- Admission_Deposit: The deposit paid by the patient during admission
- Stay (in days): The number of days that the patient has stayed in the hospital. This is the target variable
- Available Extra Rooms in Hospital: The number of rooms available during admission
- Department: The department which will be treating the patient
- Ward_Facility_Code: The code of the ward facility in which the patient will be admitted
- doctor_name: The doctor who will be treating the patient
- staff_available: The number of staff who are not occupied at the moment in the ward


### Approach to solve the problem:
1. Import the necessary libraries
2. Read the dataset and get an overview
3. Exploratory data analysis - a. Univariate b. Bivariate
4. Data preprocessing if any
5. Define the performance metric and build ML models
6. Checking for assumptions
7. Compare models and determine the best one
8. Observations and business insights