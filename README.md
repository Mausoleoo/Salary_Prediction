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

## YouTube Project Walk-Through

https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

## Steps

1.- Run Get_info.py to get the data from glassdoor. (It uses functions from Glassdoor_Scraper.py)

    It will create a CSV file (data scientist.csv)

2.- Run Data Cleaning.ipynb to clean the CSV file. 

    It will create another CSV file (data scientist cleaned.csv)
