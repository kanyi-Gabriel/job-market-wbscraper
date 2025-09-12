# Remote Job Market Analysis (Web Scraping + EDA)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-WebScraping-yellow?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly&logoColor=white)

---

## 📖 Project Overview
This project demonstrates **end-to-end web scraping, data cleaning, and analysis** of remote job postings.  
We collected live job postings from **[RemoteOK](https://remoteok.com/)** using Selenium, structured the dataset, and performed **Exploratory Data Analysis (EDA)** to extract actionable insights.


---

##  Objectives
- Scrape **job postings** (title, company, skills, salary, location, posting date).  
- Clean and normalize messy text fields (skills, salaries, locations).  
- Flatten skills into analyzable format.  
- Perform **EDA with visualizations**:
  - Most in-demand skills  
  - Top hiring companies  
  - Job location breakdown  
  - Salary distribution  
  - Job postings trend over time  

---


## 📂 Project Structure

┣ 📜 README.md

┣ 📜 requirements.txt

┣ 📂 notebooks
┃ ┗ 📓 web-scrap.ipynb

┣ 📂 data
┃ ┗ remoteok_jobs.csv

┗ 📂 images
  ┣ top_skills.png
  ┣ salary_distribution.png
  ┗ jobs_trend.png

