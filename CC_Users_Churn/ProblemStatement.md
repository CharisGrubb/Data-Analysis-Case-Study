## Problem Statement
The Thera bank recently saw a steep decline in the number of credit card users. Credit cards are a good source of money for banks because of several types of fees charged by the banks, such as annual fees, balance transfer costs, cash advance fees, late payment fees, international transaction fees, and others. Some costs are assessed to all users regardless of consumption, while others are assessed only under specific conditions.

Customers leaving credit card services would result in a loss for the bank, so the bank wants to analyse customer data to identify customers who will leave their credit card services and the reasons for doing so – so that the bank can improve in those areas.

You as a Data scientist at Thera bank need to come up with a classification model that will help the bank improve its services so that customers do not renounce their credit cards. **You need to identify the best possible model that will give the required performance.**


### Dataset Description
CLIENTNUM - Client number. Unique identifier for the customer holding the account
Attrition_Flag - Internal event (customer activity) variable - if the account is closed then "Attrited Customer" else "Existing Customer"
Customer_Age - Age in Years
Gender - Gender of the account holder
Dependent_count - Number of dependents
Education_Level - Educational Qualification of the account holder - Graduate, High School, Unknown, Uneducated, College(refers to college student), Post-Graduate, Doctorate
Marital_Status - Marital Status of the account holder
Income_Category - Annual Income Category of the account holder
Card_Category - Type of Card
Months_on_book - Period of relationship with the bank (in months)
Total_Relationship_Count - Total no. of products held by the customer
Months_Inactive_12_mon - No. of months inactive in the last 12 months
Contacts_Count_12_mon - No. of Contacts in the last 12 months
Credit_Limit - Credit Limit on the Credit Card
Total_Revolving_Bal - Total Revolving Balance on the Credit Card
Avg_Open_To_Buy - Open to Buy Credit Line (Average of last 12 months)
Total_Amt_Chng_Q4_Q1 - Change in Transaction Amount (Q4 over Q1)
Total_Trans_Amt - Total Transaction Amount (Last 12 months)
Total_Trans_Ct - Total Transaction Count (Last 12 months)
Total_Ct_Chng_Q4_Q1 - Change in Transaction Count (Q4 over Q1)
Avg_Utilization_Ratio - Average Card Utilization Ratio

**What is a Revolving Balance?**
If we don't pay the balance of the revolving credit account in full every month, the unpaid portion carries over to the next month. That's called a revolving balance.

**What is the Average Open to buy?**
'Open to Buy' means the amount left on your credit card to use. Now, this column represents the average of this value for the last 12 months.

**What is the Average utilization Ratio?**
The Avg_Utilization_Ratio represents how much of the available credit the customer spent. This is useful for calculating credit scores.

_Relation b/w Avg_Open_To_Buy, Credit_Limit and Avg_Utilization_Ratio:_

( Avg_Open_To_Buy / Credit_Limit ) + Avg_Utilization_Ratio = 1