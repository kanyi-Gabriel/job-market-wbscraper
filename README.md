# Remote Job Market Analysis (Web Scraping + EDA)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly&logoColor=white)

---

##  Project Overview
This project demonstrates **end-to-end web scraping, data cleaning, and analysis** of remote job postings.  
We collected live job postings from **[RemoteOK](https://remoteok.com/)** using Selenium, structured the dataset, and performed **Exploratory Data Analysis (EDA)** to extract actionable insights.


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


## Project Structure
```bash
job-market-wbscraper/
│── README.md
│── requirements.txt
│── .gitignore
│
├── data/
│        ├── remoteok_jobs.csv
│        └── remoteok_jobs_2025-9-13.cvs           
│   
│
├── notebooks/           # Jupyter notebooks for analysis
│   └── web-scrap.ipynb
│
├── LICENCE               
│
├── .gitattributes
├── src/                    
│  └── scraper.py              
│
├── scraper.py
│
├── images/              
│   ├── top_skills.png
│   ├── salary_distribution.png
│   └── jobs_trend.png
│
└── reports/             
    └── summary_report.pdf
```


## 📊 Key Insights
### 🔹 Top 20 Skills in Demand
![Top Skills](images/top_skills.jpg)

> Deveoper, Design, and technical roles dominate the remote job market.

### 🔹 Salary Distribution
![Salary Distribution](images/salary_distribution.jpg)

> Most jobs fall between **$60k–120k**, with some high-paying roles exceeding $150k.

### 🔹 Job Postings Over Time
![Jobs Trend](images/jobs_trend.jpg)

> Remote job postings showed consistent demand in August but dropped sharply toward the end of the month and into September.

---
## Automation (Linux Cron Jobs)

The scraper runs daily at 9 AM using cron on WSL/Linux. Each run saves a dated CSV in /data
### Cron Setup:

1. Open cron editor:
``` bash
crontab -e
```
2. Add the following line:
```bash

0 9 * * * /usr/bin/python3 /path/to/your/project/scraper.py
```


##  Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kanyi-Gabriel/job-market-wbscraper.git
   
2. Create a virtual environment
    ```bash

   conda create -- name environment_name
   conda activate environment_name
   pip install -r requirements.txt
    
3. To add the environment to jupyter notebook
    ```bash
    conda install -c anaconda ipykernel
    python -m ipykernel install --user--name = environment_name

