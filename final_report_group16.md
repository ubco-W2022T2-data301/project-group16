# Final Report - Group 16
## **Introduction**
Our group examined the global cost of living. Within our analysis, we wished to understand the current cost to live locally in Kelowna and around the world. Due to record high inflation in 2022/23 seen throughout the world, our group was interested in seeing if we could find out where it is considered unaffordable to live and what categories influence affordability the most. Moreover, our group was interested in necessities such as food, housing and transportation costs alongside luxuries such as restaurants and accommodation. Altogether we wish to examine how the cost of living varies city-to-city/country-to-country, where the cost of living is lower/higher and finally why this is the case.

## **Exploratory Data Analysis**
Here is a summary of the highlights of our group's EDAs:

- In Robert's analysis he used a variety of plots although primarily relying on facet grids to show multiple histograms based on the cost of living indexes and scatter plots to determine where cities rank in terms of affordability. This made it clear to see the distribution of cities ranked according to their indexes. 

- For Oliver's analysis he used...TODO

- In Ken's analysis he utilized...TODO

## Research Question 1: and Results: *How livable is it in Kelowna compared to other cities globally?*

### Analysis done by **Robert Yacovelli** [here!](https://github.com/ubco-W2022T2-data301/project-group16/blob/main/analysis/analysis_yacovelli.ipynb)

### **1.1:**  *How does the cost of necessities, such as food items, transportation, and shelter vary across different cities as compared to Kelowna, serving as the baseline?*

To answer this question I first took all the relevant columns related to food, housing and transportation. I set Kelowna to be the baseline city with an index level set to 100. Any city above or below 100 represents a % change in affordability in that category. 
![Food, Housing and transport indexes](images/RYplot7.png)

Here I found that Kelowna is generally more expensive in food and housing while appearing to be cheaper in the transportation category. These visuals also provide a good look at the distribution of the indexes by city. 

![Weighted Cost of Living Index](images/RYplot8.png)

Answering the research question it is clear that after plotting the weighted cost of living Kelowna is on the right side of the distribution indicating it is generally more expensive to live in Kelowna as compared to the other cities included in the dataset. 

### **1.2:** *Can the price of a McDonald's meal tell us anything about the cost of living in a country?*

Serving as a secondary question I wanted to investigate any possible correlation between the price of a McDonald's meal and the affordability in a city and more specifically within a country.

![Cost of living indexes vs McDonald's meal](images/RYplot9.png)

According to this plot, the cost of a McDonald's meal does not accurately depict the overall affordability in a country since the Weighted Cost of Living Index by country has a correlation value of `0.47`. This is also the case for the Housing and transportation index with an even lower correlation of `0.27`. 

Where the cost of McDonald's meals may provide some estimation of affordability within a country is with the food index given there is a `0.74` correlation value. 

We can then answer this question by confirming that in this case, the price of a McDonald's meal is an okay indicator when it comes to the overall cost of food in a country. 


### **1.3:** *How do the prices of different types of transportation (public transit, taxi, personal car) vary across different countries and how does this variation relate to differences in income and cost of living?*

 The purpose of this question was to analyze whether or not when the ability to transport yourself (to your job) is cheaper and whether or not you earn more. To answer this question I took 5 richer and 5 developing countries and compared the cost of each type of transportation alongside the monthly salary for each country.

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

## Research Question 3 and Result:   How the cost of other stuff, which are considered not necessary for living, different between cities in Canada?

### Analysis done by **Kenta Selim Ishida** [here](https://github.com/ubco-W2022T2-data301/project-group16/blob/main/analysis/analysis_ishida.ipynb)
These 3 following questions helps to answer RQ3, and to get deeper understanding for RQ3. 
### 3.1: If there are differences, is there any factors for the difference?
To answer this question, I will first show the bar plots of cost of items categorized by type in various Canadian cities.
![Expensive Accommodations Barplot](images/IKplot3.png)
![Entertainment Barplot](images/IKplot4.png)

These visualizations reveal that the costs are different between cities even they are both cities in Canada. Moreover, it is obvious that the disparties are big for some categories, but for some categories the disparties are neligible. We found that there are differences between cities, so we will now find the factors for the differences using heatmap.

![Luxuaries Heatmap](images/IKplot5.png)

The heatmap presented depicts the correlation between each pair of columns within the dataset. The visual representation effectively showcases the strength of correlations between various columns, with notable correlations observed between food and accommodation, food and population, accommodation and density, and entertainment and net salary. These findings suggest that there exist discernible factors contributing to cost discrepancies, and furthermore, that such factors may vary across distinct categories.

### 3.2: Do values of daily necessities affects the value of other stuff?

To answer this question,  I conducted a comparative analysis between each luxury item and its corresponding necessity within the same category. I have included plots of two remarkable findings that have emerged from my research in this section.

![Accommodations Scatterplot](images/IKplot14.png)

The plot above is a scatter plot of price of accommodations sorted into two categories of inexpensive expensive options with a linear trendline. Here I found the prices of inexpensive accommodations and expensive accommodations are in direct proportion.

![Transportation Scatterplot](images/IKplot13.png)

The plot above is a scatter plot of price of transportation sorted into two categories of inexpensive expensive options with a linear trendline. I personally think this is the most interesting fact I have found in my entire research. Surprisingly, the prices of inexpensive transportation and expensive transportation are in inverse proportion.


### 3.3: Which luxuary shows the general cost of luxuaries the best?

To answer this question, I first plotted correlations between each categories and general cost of luxuaries.

![Luxuaries + General Heatmap](images/IKplot11.png)

The most bottom raw dispicts the correlations that I wanted. Obviously, price of food and accommodation have strong correlation to price of luxuaries in general. Especially, the price of accommodation has correlation of over 0.9, which can be cosidered as a indicator of the price of luxuaries in general. The scatter plot below illustrates the relationship between those two.

![Expensive Accommodatin vs General Luxuaries Scatterplot](images/IKplot12.png)

### Summary RQ3:
    - There are difference of costs of luxuaries between Canadian cities, and factors vary across categories.
    - For some categories the price of necessities to the same categories of luxuaries. However, the relations are not the same for all categories.
    - The price of expensive accommodations can be an indicator of the cost of luxuaries in general.

## Conclusion TODO
 A brief paragraph that highlights your key results and what you learned from doing this project.
