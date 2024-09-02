import requests
from bs4 import BeautifulSoup

def scrape_linkedin_jobs(keywords, location):
  url = f"https://www.linkedin.com/jobs/search?keywords={keywords}&location={location}"

  # Send HTTP GET request and get the HTML content
  response = requests.get(url)
  html_content = response.content

  # Parse the HTML content with Beautiful Soup
  soup = BeautifulSoup(html_content, 'html.parser')

  # Find all job card elements
  job_cards = soup.find_all('li', class_='job-card-list__item')

  # Extract data from each job card
  jobs = []
  for card in job_cards:
    job_dict = {}

    # Extract job title
    job_title_tag = card.find('h3', class_='job-card-profile__title')
    if job_title_tag:
      job_dict['title'] = job_title_tag.text.strip()

    # Extract company name
    company_tag = card.find('h4', class_='job-card-profile__company')
    if company_tag:
      job_dict['company'] = company_tag.text.strip()

    # Extract location
    location_tag = card.find('span', class_='job-card-profile__location')
    if location_tag:
      job_dict['location'] = location_tag.text.strip()

    # Add the job dictionary to the list of jobs
    if job_dict:
      jobs.append(job_dict)

  # Return the list of jobs
  return jobs

# Define keywords and location (as comma-separated strings)
keywords = "data analyst, Business Analyst, Quality Analyst"
location = "Bangalore, Remote"

# Scrape jobs and store them in the "jobs" list
jobs = scrape_linkedin_jobs(keywords, location)

# Print the scraped jobs
for job in jobs:
  print(f"Title: {job.get('title')}")
  print(f"Company: {job.get('company')}")
  print(f"Location: {job.get('location')}")
  print("-" * 20)
