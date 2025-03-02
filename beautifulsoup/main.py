from bs4 import BeautifulSoup
import requests
import time


print("Insert Skills")
unfamiliar_skill = input('>')

print(f"filtering out {unfamiliar_skill}")

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'srp-job-bx')

def find_jobs():
    for job in jobs:
        company_name = job.find('span', class_ = 'srp-comp-name').text.strip()
        skill_requirements = job.find('div', class_ = 'srp-keyskills').text.strip()
        more_info = job.h3.a['href']
        published_date = job.find('span', class_ = 'posting-time').text.strip()
        if unfamiliar_skill.lower() not in skill_requirements.lower():
            with open(f'posts/jobs.txt', 'a') as f:
                f.write(f'''
                    Company Name : {company_name}
                    Required Skills : {skill_requirements}
                    Posting Time : {published_date}
                    More Info : {more_info}
                    ''')


find_jobs()