import time
from typing import List

import pandas as pd
import requests
from bs4 import BeautifulSoup


class GreenhouseScraper:
    def __init__(self, company_slug: str):
        self.company_slug = company_slug
        self.base_url = f"https://job-boards.greenhouse.io/{company_slug}"

    def fetch_html(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=20,
        )
        response.raise_for_status()

        return response.text

    def parse_job_links(self, html: str) -> pd.DataFrame:
        soup = BeautifulSoup(html, "lxml")
        job_rows = []

        links = soup.find_all("a", href=True)

        for link in links:
            title = link.get_text(strip=True)
            href = link["href"]

            if not title:
                continue

            if "/jobs/" not in href:
                continue

            if href.startswith("/"):
                job_url = f"https://job-boards.greenhouse.io{href}"
            else:
                job_url = href

            job_rows.append(
                {
                    "company": self.company_slug,
                    "title": title,
                    "job_url": job_url,
                    "source": "greenhouse",
                }
            )

        jobs = pd.DataFrame(job_rows)

        if jobs.empty:
            return jobs

        jobs = jobs.drop_duplicates(subset=["job_url"])

        return jobs

    def fetch_job_description(self, job_url: str) -> str:
        html = self.fetch_html(job_url)
        soup = BeautifulSoup(html, "lxml")

        text = soup.get_text(
            separator=" ",
            strip=True,
        )

        return text

    def scrape(self) -> pd.DataFrame:
        board_html = self.fetch_html(self.base_url)
        jobs = self.parse_job_links(board_html)

        if jobs.empty:
            return jobs

        descriptions: List[str] = []

        for job_url in jobs["job_url"]:
            try:
                description = self.fetch_job_description(job_url)
            except Exception:
                description = ""

            descriptions.append(description)
            time.sleep(0.5)

        jobs["description"] = descriptions
        jobs["job_id"] = range(1, len(jobs) + 1)
        jobs["location"] = "Unknown"
        jobs["remote_type"] = "Unknown"

        return jobs