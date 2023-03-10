from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import time


def fetch_jobs(keyword, num_pages, path):
    options = Options()
    options.add_argument("window-size=1920,1080")
    #Enter your chromedriver.exe path below
    chrome_path = path
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    #url = 'https://www.glassdoor.ca/Job/canada-' + keyword + '-jobs-SRCH_IL.0,6_IN3_KO7,19.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=Canada&context=Jobs&dropdown=0'
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    url = 'https://www.glassdoor.ca/Job/canada-jobs-SRCH_IL.0,6_IN3.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=Canada&context=Jobs&dropdown=0'
    driver.get(url)
    search_input = driver.find_element(By.ID,"sc.keyword")
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)
    time.sleep(2)
    
    
    
    
    company_name = []
    job_title = []
    salary_est = []
    location = []
    job_description = []
    salary_min = []
    salary_max = []
    salary_estimate = []
    company_size = []
    company_type = []
    company_sector = []
    company_industry = []
    company_founded = []
    company_revenue = []
    
    
    
    #Set current page to 1
    current_page = 1     
        
        
    time.sleep(3)
    
    while current_page <= num_pages:   
        time.sleep(3)
        
        try:
            driver.find_element(By.CLASS_NAME,"selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)
    
        try:
            driver.find_element(By.CLASS_NAME,"ModalStyle__xBtn___29PT9").click()  #clicking to the X.
        except NoSuchElementException:
            pass
        done = False
        print('3')
        while not done:
            job_cards = driver.find_elements(By.XPATH,"//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")
        
            
            for card in job_cards:
                try:
                    card.click()
                    time.sleep(1)
                    
                    #Closes the signup prompt
                    try:
                        driver.find_element(By.XPATH,".//span[@class='SVGInline modal_closeIcon']").click()
                        time.sleep(2)
                    except NoSuchElementException:
                        time.sleep(2)
                        pass

                    #Expands the Description section by clicking on Show More
                    try:
                        driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb4']").click()                                                                
                        time.sleep(1)
                    except NoSuchElementException:
                        card.click()
                        print(str(current_page) + '#ERROR: no such element')
                        time.sleep(30)
                        driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb2']").click()
                    except ElementNotInteractableException:
                        card.click()
                        driver.implicitly_wait(30)
                        print(str(current_page) + '#ERROR: not interactable')
                        driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb2']").click()

                    #Scrape 

                    try:
                        company_name.append(driver.find_element(By.XPATH,"//div[@class='css-87uc0g e1tk4kwz1']").text)
                    except:
                        company_name.append("-1")
                        pass

                    try:
                        job_title.append(driver.find_element(By.XPATH,"//div[@class='css-1vg6q84 e1tk4kwz4']").text)
                    except:
                        job_title.append("-1")
                        pass

                    try:
                        location.append(driver.find_element(By.XPATH, "//div[@class='css-56kyx5 e1tk4kwz5']").text)
                    except:
                        location.append("-1")
                        pass

                    try:
                        job_description.append(driver.find_element(By.XPATH,"//div[@id='JobDescriptionContainer']").text)
                    except:
                        job_description.append("-1")
                        pass

                    
                    try:
                        salary_estimate.append(driver.find_element(By.XPATH,"//div[@class='css-1bluz6i e2u4hf13']").text)
                    except:
                        salary_estimate.append("-1")
                        pass

                    
                    try:
                        company_size.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Size']//following-sibling::*").text)
                    except:
                        company_size.append("-1")
                        pass
                    
                    try:
                        company_type.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Type']//following-sibling::*").text)
                    except:
                        company_type.append("-1")
                        pass
                        
                    try:
                        company_sector.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Sector']//following-sibling::*").text)
                    except:
                        company_sector.append("-1")
                        pass
                        
                    try:
                        company_industry.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Industry']//following-sibling::*").text)
                    except:
                        company_industry.append("-1")
                        pass
                        
                    try:
                        company_founded.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Founded']//following-sibling::*").text)
                    except:
                        company_founded.append("-1")
                        pass
                        
                    try:
                        company_revenue.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Revenue']//following-sibling::*").text)
                    except:
                        company_revenue.append("-1")
                        pass

                    
                except:
                    pass
                    
                    
                    
                    
                done = True
       # Moves to the next page         
        if done:
            print(str(current_page) + ' ' + 'out of' +' '+ str(num_pages) + ' ' + 'pages done')
            driver.find_element(By.XPATH,"//span[@alt='next-icon']").click()   
            current_page = current_page + 1
            time.sleep(4)
            




    driver.close()
    df = pd.DataFrame({'company': company_name, 
    'job title': job_title,
    'location': location,
    'job description': job_description,
    'salary estimate': salary_estimate,
    'company_size': company_size,
    'company_type': company_type,
    'company_sector': company_sector,
    'company_industry' : company_industry, 
    'company_founded' : company_founded, 
    'company_revenue': company_revenue})
    
    df.to_csv(keyword + '_Canada.csv')
                       