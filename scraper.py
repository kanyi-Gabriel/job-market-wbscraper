# scraper.py  (at the root)

from src.scraper import scrape_jobs
from datetime import date

# Run scraper
df = scrape_jobs()

# Save with today's date
today = date.today().isoformat()
output_file = f"data/remoteok_jobs_{today}.csv"
df.to_csv(output_file, index=False)

print(f"Scraped {len(df)} jobs on {today} → saved to {output_file}")
