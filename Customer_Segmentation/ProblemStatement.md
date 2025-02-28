## Business Context
Understanding customer personality and behavior is pivotal for businesses to enhance customer satisfaction and increase revenue. Segmentation based on a customer's personality, demographics, and purchasing behavior allows companies to create tailored marketing campaigns, improve customer retention, and optimize product offerings.

A leading retail company with a rapidly growing customer base seeks to gain deeper insights into their customers' profiles. The company recognizes that understanding customer personalities, lifestyles, and purchasing habits can unlock significant opportunities for personalizing marketing strategies and creating loyalty programs. These insights can help address critical business challenges, such as improving the effectiveness of marketing campaigns, identifying high-value customer groups, and fostering long-term relationships with customers.

With the competition intensifying in the retail space, moving away from generic strategies to more targeted and personalized approaches is essential for sustaining a competitive edge.

## Objective
In an effort to optimize marketing efficiency and enhance customer experience, the company has embarked on a mission to identify distinct customer segments. By understanding the characteristics, preferences, and behaviors of each group, the company aims to:

Develop personalized marketing campaigns to increase conversion rates.
Create effective retention strategies for high-value customers.
Optimize resource allocation, such as inventory management, pricing strategies, and store layouts.
As a data scientist tasked with this project, your responsibility is to analyze the given customer data, apply machine learning techniques to segment the customer base, and provide actionable insights into the characteristics of each segment.

## Data Dictionary
The dataset includes historical data on customer demographics, personality traits, and purchasing behaviors. Key attributes are:

#### Customer Information

- ID: Unique identifier for each customer.
- Year_Birth: Customer's year of birth.
- Education: Education level of the customer.
- Marital_Status: Marital status of the customer.
- Income: Yearly household income (in dollars).
- Kidhome: Number of children in the household.
- Teenhome: Number of teenagers in the household.
- Dt_Customer: Date when the customer enrolled with the company.
- Recency: Number of days since the customer’s last purchase.
- Complain: Whether the customer complained in the last 2 years (1 for yes, 0 for no).

##### Spending Information (Last 2 Years)
- MntWines: Amount spent on wine.
- MntFruits: Amount spent on fruits.
- MntMeatProducts: Amount spent on meat.
- MntFishProducts: Amount spent on fish.
- MntSweetProducts: Amount spent on sweets.
- MntGoldProds: Amount spent on gold products.
- Purchase and Campaign Interaction

- NumDealsPurchases: Number of purchases made using a discount.
- AcceptedCmp1: Response to the 1st campaign (1 for yes, 0 for no).
- AcceptedCmp2: Response to the 2nd campaign (1 for yes, 0 for no).
- AcceptedCmp3: Response to the 3rd campaign (1 for yes, 0 for no).
- AcceptedCmp4: Response to the 4th campaign (1 for yes, 0 for no).
- AcceptedCmp5: Response to the 5th campaign (1 for yes, 0 for no).
- Response: Response to the last campaign (1 for yes, 0 for no).

##### Shopping Behavior

- NumWebPurchases: Number of purchases made through the company’s website.
- NumCatalogPurchases: Number of purchases made using catalogs.
- NumStorePurchases: Number of purchases made directly in stores.
- NumWebVisitsMonth: Number of visits to the company’s website in the last month.