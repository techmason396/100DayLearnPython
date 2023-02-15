
from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://www.careerlink.vn/tim-viec-lam-tai/binh-thuan/BT?posted_within=1")

html = response.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.title

list_new_job = soup.select(
    selector=".list-group .job-item .job-link")

title_new_jobs = []
link_new_jobs = []

for job in list_new_job:
    title_new_jobs.append(job.getText().strip())
    link_new_jobs.append("https://www.careerlink.vn"+job.get('href'))

print(title_new_jobs)
# print(link_new_jobs)
