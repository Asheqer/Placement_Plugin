import re
from CONSTANTS import MONTHS
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from plugin_queries import check_duplicates_query,insert_placement_records_query, select_placements_query, select_placements_query, insert_single
from add_placements_to_db import db_conn


options = Options()
options.add_argument('--headless')

records = []

url = "https://www.ratemyplacement.co.uk/search-jobs/placement"

def format_date(date):
    match = re.search(r'(\d{1,2})\w{2} (\w+) (\d{4})', deadline_element)
    return f"{match.group(3)}-{MONTHS.get(match.group(2))}-{match.group(1)}"

try:
    driver = webdriver.Chrome(options=options, service=ChromeService(
        ChromeDriverManager().install()))
    driver.get(url)

    elements = driver.find_elements(By.CLASS_NAME, "Search-content")

    for placement in elements:
        name_element = placement.find_element(By.TAG_NAME, "h2").text
        company_element = placement.find_element(By.CLASS_NAME, "Search-industry").text
        deadline_element = placement.find_element(By.CLASS_NAME, "deadline").text.strip("Deadline: ")
        duration_element = placement.find_element(By.CLASS_NAME, "duration").text
        location_element = placement.find_element(By.CLASS_NAME, "company").text
        formatted_deadline = format_date(deadline_element)
        if db_conn.execute_query(check_duplicates_query, (name_element,))[0][0] == 0:
            records.append((name_element, company_element, formatted_deadline, duration_element, location_element))
except Exception as e:
    print("Error during web scraping:", e)
finally:
    if 'driver' in locals():
        driver.quit()
if records:
    try:
        for element in records:
            db_conn.execute_query(insert_placement_records_query, element)
    except Exception as e:
        print("Error inserting records into the database:", e)
else:
    print("There are no new entries")