# Final Report - Group 16

## **Introduction** TODO
A short paragraph introducing your project to the audience and a motivation for why this project is important. It’s fine to say your group has an interest in this topic and were keen to explore it more.

## **Exploratory Data Analysis** TODO
A summary of the highlights of your EDA, where you can show some visualizations of the exploratory data analysis your group did.

## Research Question 1: and Results: *How livable is it in Kelowna compared to other cities globally?*

### Analysis done by **Robert Yacovelli** [here!](https://github.com/ubco-W2022T2-data301/project-group16/blob/main/analysis/analysis_yacovelli.ipynb)

### **1.1:**  *How does the cost of necessities, such as food items, transportation, and shelter vary across different cities as compared to Kelowna, serving as the baseline?*

In order to answer this question I first took all the relevant columns related to food, housing and transportation. I set Kelowna to be the baseline city with an index level set to 100. Any city above or below 100 represents a % change in affordability in that category. 
![Food,Housing and transport indexes](images/RYplot7.png)

Here I found that Kelowna is generally more expensive in food and housing while appearing to be cheaper in the transportation category. These visuals also provide a good look at the distribution of the indexes by city. 

![Weighted Cost of Living Index](images/RYplot8.png)

Answering the research question it is is clear that after plotting the weighted cost of living Kelowna is on the right side of the distribution indicating it is generally more expensive to live in Kelowna as compared to the other cities included in the dataset. 

### **1.2:** *Can the price of a McDonald's meal tell us anything about the cost of living in a country?*

Serving as a secondary question I wanted to investigate any possible correlation between the price of a McDonald's meal and the affordability in a city and more specifically within a country.

![Cost of living indexes vs McDonald's meal](images/RYplot9.png)

According to this plot the cost of a McDonald's meal does not accurately depict the overall affordability in a country since the Weighted Cost of Living Index by country has a correlation value of `0.47`. This is also the case for the Housing and transportation index with an even lower correlation of `0.27`. 

Where the cost of McDonald's meal may provide some estimation on affordability within a country is with the food index given there is a `0.74` correlation value. 

We can then answer this question by confirming that in this case the price of a McDonald's meal is an okay indicator when it comes to the overall cost of food in a country. 


### **1.3:** *How do the prices of different types of transportation (public transit, taxi, personal car) vary across different countries and how does this variation relate to differences in income and cost of living?*

 The purpose of this question was to analyze whether or not when the ability to transport yourself (to your job) is cheaper whether or not you earn more. To answer this question I took 5 richer and 5 developing countries and compared the cost of each type of transportation alongside the monthly salary for each country.

![Transport types and monthly salary 10 countries](images/RYplot10.png)

The main takeaway from this plot and the answer to this question was that cheaper transportation does not equate to a higher salary. Another plot was done in the [analysis](https://github.com/ubco-W2022T2-data301/project-group16/blob/main/analysis/analysis_yacovelli.ipynb) to verify that this was also the case for ALL countries in the dataset. 

### Summary RQ1: 
     - Kelowna is generally more expensive and a less affordable city to live in. 
     - The price of a McDonald's meal is an okay indicator when it comes to the overall cost of food in a country.
     - Cheaper transportation does not equate to a higher salary.

## Research Question 2 and Results:

### 2.1


### 2.2


### 2.3 

## Research Question 3 and Results: How the cost of other stuff, which are considered not necessary for living, different between cities in Canada?

### 3.1: Is there any factors for that?


### 3.2: Do values of daily necessities affects the value of other stuff?


### 3.3: Which luxuary shows the general cost of luxuaries the best?

## Conclusion TODO
 A brief paragraph that highlights your key results and what you learned from doing this project.
