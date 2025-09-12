# Remote Job Market Analysis (Web Scraping + EDA)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium&logoColor=white)
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

  
---

## 📊 Key Insights
### 🔹 Top 20 Skills in Demand
![Top Skills](images/top_skills.png)

> Python, AWS, and SQL dominate the remote data science job market.

### 🔹 Salary Distribution
![Salary Distribution](images/salary_distribution.png)

> Most jobs fall between **$60k–120k**, with some high-paying roles exceeding $150k.

### 🔹 Job Postings Over Time
![Jobs Trend](images/jobs_trend.png)

> Remote job postings show consistent demand, peaking in the last month.

---

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/<kanyi-Gabriel>/job-market-wbscraper.git
 


