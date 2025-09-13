from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_jobs(url="https://remoteok.com/remote-data-scientist-jobs"):
    """Scrape jobs from RemoteOK and return a DataFrame."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(5)

    job_rows = driver.find_elements(By.CSS_SELECTOR, "tr.job")
    jobs = []
    for row in job_rows:
        try:
            title = row.find_element(By.TAG_NAME, "h2").text
            company = row.find_element(By.TAG_NAME, "h3").text
            date_posted = row.find_element(By.TAG_NAME, "time").get_attribute("datetime")
            tags = [tag.text for tag in row.find_elements(By.CSS_SELECTOR, ".tag")]
            locations = row.find_elements(By.CSS_SELECTOR, ".location")
            location = locations[0].text if len(locations) > 0 else None
            salary = locations[1].text if len(locations) > 1 else None

            jobs.append({
                "title": title,
                "company": company,
                "date_posted": date_posted,
                "tags": tags,
                "location": location,
                "salary": salary
            })
        except:
            pass

    driver.quit()
    return pd.DataFrame(jobs)
