from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize the driver (no need to specify executable_path if ChromeDriver is in PATH)
driver = webdriver.Chrome()

# Open the Naukri website
driver.get('https://www.naukri.com')

# Wait for the page to load
time.sleep(20)

# Input data into the search fields
search_input = driver.find_element(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
search_input.send_keys('Data Analysis')

location_input = driver.find_element(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
location_input.send_keys('Mumbai')

# Click the search button
search_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[6]')
search_button.click()

# Wait for the job listings to appear
time.sleep(5)

# List to store job data
all_jobs = []

# Loop through pages until page 5
for page in range(1, 6):  # Pages 1 to 5
    print(f"Scraping page {page}...")
    
    # Wait for the page to load
    time.sleep(5)
    
    # Find all job containers on the current page
    job_containers = driver.find_elements(By.XPATH, '//*[@id="listContainer"]/div[2]/div/div')
    
    # Extract data for each job container
    for job in job_containers:
        try:
            job_title = job.find_element(By.XPATH, './/div/div[1]/a').text
        except:
            job_title = "Not Available"
        
        try:
            company_name = job.find_element(By.XPATH, './/div/div[2]/span/a[1]').text
        except:
            company_name = "Not Available"
        
        try:
            location = job.find_element(By.XPATH, './/div/div[3]/div/span[3]/span/span').text
        except:
            location = "Not Available"
        
        try:
            salary = job.find_element(By.XPATH, './/div/div[3]/div/span[2]/span/span').text
        except:
            salary = "Not Available"
        
        try:
            experience = job.find_element(By.XPATH, './/div/div[3]/div/span[1]/span/span').text
        except:
            experience = "Not Available"
        
        # Append job details to the list
        all_jobs.append({
            "Job Title": job_title,
            "Company Name": company_name,
            "Location": location,
            "Salary": salary,
            "Experience": experience
        })
    
    # Find the 'Next' button or pagination element and click it
    try:
        next_button = driver.find_element(By.XPATH, '//*[@id="lastCompMark"]/div[2]/a[1]')
        next_button.click()
    except:
        print("No more pages found.")
        break

# Save the job data to a CSV file using pandas
df = pd.DataFrame(all_jobs)
df.to_csv('job_listings.csv', index=False)

print(f"Scraped data saved to 'job_listings.csv'.")

# Close the driver
driver.quit()
