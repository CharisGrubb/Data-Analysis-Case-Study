## Context and Problem Statement
Active investing in the asset management industry aims to beat the stock market’s average returns, for which portfolio managers track a particular index and try to beat that index by creating their own portfolios.

Portfolio construction involves selection of stocks that have a higher probability of giving better returns in comparison to the tracking index, like S&P 500. In this project, we will use the concept of Network Analysis to select a basket of stocks and create two portfolios. We will then simulate portfolio value by investing a certain amount, keeping the portfolio for an entire year and we will then compare it against the S&P 500 index.

In this project we will try to follow the approach mentioned in the below research paper:

Dynamic portfolio strategy using a clustering approach

## Proposed Approach
Collect the price data for all S&P 500 components from 2011 till 2020
Compute log returns for the S&P 500 components for same time period
Compute the correlation matrix for the above log returns
Find out the Top n central and peripheral stocks based on the following network topological parameters:
Degree centrality
Betweenness centrality
Distance on degree criterion
Distance on correlation criterion
Distance on distance criterion
Simulate the performance of central and peripheral portfolios against the performance of S&P 500 for the year 2021

