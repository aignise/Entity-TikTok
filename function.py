import os
from dotenv import load_dotenv
import requests
from openai import OpenAI

load_dotenv()

url = "https://jsearch.p.rapidapi.com/search"
headers = {
    "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_jobs(query, page=1, num_pages=3, date_posted="all", remote_jobs_only=False,
                employment_types=None, job_requirements=None, job_titles=None, company_types=None,
                employers=None, actively_hiring=False, radius=None, categories=None, country="us",
                language="en", exclude_job_publishers=None):

    querystring = {
        "query": query,
        "page": page,
        "num_pages": num_pages,
        "date_posted": date_posted,
        "remote_jobs_only": str(remote_jobs_only).lower(),
        "employment_types": employment_types,
        "job_requirements": job_requirements,
        "job_titles": job_titles,
        "company_types": company_types,
        "employers": employers,
        "actively_hiring": str(actively_hiring).lower(),
        "radius": radius,
        "categories": categories,
        "country": country,
        "language": language,
        "exclude_job_publishers": exclude_job_publishers
    }

    # Remove None values from querystring
    querystring = {k: v for k, v in querystring.items() if v is not None}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
