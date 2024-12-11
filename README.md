# Data Science Salary Prediction Estimator in Canada

- Created a tool that estimates data science salaries (MAE ~ $ 2.8k) to help data scientists negotiate their income when they get a job.

- Scraped over 450 job descriptions from glassdoor Canada using python and selenium

- Engineered features from the text of each job description to quantify the value companies put on Python, SAS, Spark, Matlab, Hadoop, Tensorflow, Pytorch and Tableau.
 
- Optimized Linear, Lasso and Random Forest Regressors using GridsearchCV to reach the best model.



## Resources
**Python Version**: 3.9.13

**Packages**: Pandas, NumPy, Matplotlib, Seaborn, Selenium==4.8.0, Wordcloud==1.8.2.2

**Tutorial**: https://github.com/PlayingNumbers/ds_salary_proj

**Glassdoor Scraper**: https://github.com/rohan-benjamin/Glassdoor-Scraper-Final

**Glassdoor Scraper Article**: https://medium.com/@benjaminrohan010/scraping-glassdoor-using-selenium-and-python-2022-bd0065775aec


## Steps

1.- Run Get_info.py to get the data from glassdoor. (It uses functions from Glassdoor_Scraper.py)

    It will create a CSV file (data scientist Canada.csv)

2.- Run Data Cleaning.ipynb to clean the CSV file. 

    It will create another CSV file (data scientist Canada cleaned.csv)
    
    > After cleaning the data, the following columns were obtained from each job.
    * Estimated salary
    * Company
    * Job title
    * Location
    * Job description
    * Company size
    * Company type
    * Company sector
    * Company industry
    * Age
    * Company revenue
    * Rating
    * Python is needed
    * SAS is needed
    * Tableau is needed
    * Matlab is needed
    * Spark is needed
    * Tensorflow is needed
    * Pytorch is needed
    * Hadoop is needed
    * Seniority
    * Title Simplified
   
3.- Run Data_EDA.ipynb to Data Analysis (Exploratory Data Analysis)

    Data distribution as well as counts of values for categorical variables were analyzed and examined. 
    The following are a few highlights from the pivot tables.
    
    
   ![graph_cities](https://user-images.githubusercontent.com/21091686/220508186-e3c395db-c3a6-4d6e-bfeb-53c03c043644.png)

   ![seniority_estimated_salary](https://user-images.githubusercontent.com/21091686/220508562-970f7bd4-90b3-4aeb-ae53-40b6e6b605f3.png)

   ![frequent_words](https://user-images.githubusercontent.com/21091686/220508684-d363ead1-df1b-4f10-8fc9-96b8dddc0005.png)
   
4.- Run Model Building.ipynb to train and test models
    
    a) The categorical variables were created into dummy variables and the data were split into training and test.
    
    b) Three different models were compared: Multiple Linear Regression, Lasso Regression and Random Forest.
       The models were evaluated using Mean Absolute Error.
       
5.- Model Performance
    
    - Multiple Linear Regression: MAE = 23,764.03
    - Lasso Regression: MAE = 3,211.27
    - Random Forest: MAE = 2,832.47


## YouTube Project Walk-Through

https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
