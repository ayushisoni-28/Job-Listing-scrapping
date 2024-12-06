# Job Listings Scraper

## Project Description
This project scrapes job listings from the Naukri website using **Selenium** and **Python**. The scraper extracts job details like job title, company name, location, salary, and required experience from Naukri.com. It then navigates through multiple pages of job listings and stores the scraped data in a **CSV** file for further analysis.

## Requirements
- Python 3.x
- Selenium
- Pandas
- ChromeDriver (compatible version with Chrome)

## Setup
1. Install required libraries:
   ```bash
   pip install selenium pandas

2. Download ChromeDriver: Ensure you have ChromeDriver installed and accessible in your system PATH.

## Project Overview
### 1. Initialize the Web Driver
The script uses Selenium's webdriver to open the Chrome browser and navigate to the Naukri website.

### 2. Input Search Parameters
The script inputs a job title ("Data Analysis") and location ("Mumbai") into the search fields on Naukri's homepage.
The search is triggered by clicking the search button.

### 3. Extract Job Listings
The script iterates through the search results, scraping job details (job title, company name, location, salary, and experience) from each job listing on the page.
It handles missing data gracefully using try-except blocks to ensure that the scraper doesn't fail if some details are unavailable.

### 4. Pagination
The script navigates through multiple pages (pages 1 to 5) by clicking the "Next" button until it reaches the specified page limit.
### 5. Storing Data
The scraped data is stored in a list of dictionaries, which is then converted into a pandas DataFrame.
The data is saved into a CSV file (job_listings.csv), making it easy to use for analysis.
### 6. End the Session
After scraping the job listings, the browser session is closed with driver.quit().

## Brief Explanation to run the code:
Step 1: Install the necessary libraries (selenium, pandas).

Step 2: Download and set up ChromeDriver.

Step 3: Save the script as scraper.py and run it.

Step 4: Monitor the output in the terminal and check the CSV file for scraped data.
