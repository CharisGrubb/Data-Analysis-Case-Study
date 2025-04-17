**The Hidden Markov Model (HMM)** is a probabilistic model that is used to explain or derive the probability of any random process. It basically states that an observed event will be related to a set of probability distributions rather than its step-by-step status. Assume the system being modelled is a Markov chain, with some hidden states in the process. In that case, hidden states are a process that is dependent on the main Markov process/chain.

The primary goal of the HMM is to discover information about a Markov chain by observing its hidden states. Considering a Markov process X with hidden states Y, the HMM establishes that the probability distribution of Y for each time stamp must not be dependent on the history of X at that time.

## Case Study - Context
The CES program is a monthly survey conducted by the Bureau of Labor Statistics. The program provides employment, hours, and earnings estimates based on payroll records of business establishments. Data produced from the CES survey include nonfarm employment series for all employees, production and nonsupervisory employees, and women employees, as well as average hourly earnings, average weekly hours, monthly umemployment rate and average weekly overtime hours (in manufacturing industries) for both all employees and production and nonsupervisory employees. Labor Force Data comes from the 'Current Population Survey (Household Survey)'.

The Unemployment Rate represents the number of unemployed as a percentage of the labor force.

This rate is also defined as the U-3 measure of labor underutilization.

## Objective
In this notebook, we'll look at how to use Hidden Markov Models (HMM) to predict the Unemployment Rate over the years. Using a HMM, we will predict whether the unemployment rate will rise or fall each year based on the data.

When we examine the relationship between the provided data and the unemployment rate, we discover that the unemployment rate peaks whenever there is a recession/pandemic. So we are interested in how we can build Hidden Markov Models (HMM) by using the data we have to identify this. Furthermore, we want to see if our model can predict the unemployment rate more accurately.

## Dataset
We will use Unemployment Rate data from the U.S. Bureau of Labor Statistics (monthly data from 1948 to 2022).