from src.scrapers.greenhouse_scraper import GreenhouseScraper


def main():
    company_slugs = [
        "zillow",
        "dropbox",
        "stripe",
        "discord",
    ]

    all_jobs = []

    for company_slug in company_slugs:
        print(f"Scraping {company_slug}...")

        try:
            scraper = GreenhouseScraper(company_slug=company_slug)
            jobs = scraper.scrape()

            if not jobs.empty:
                all_jobs.append(jobs)
                print(f"Collected {len(jobs)} jobs from {company_slug}.")
            else:
                print(f"No jobs found for {company_slug}.")

        except Exception as error:
            print(f"Failed to scrape {company_slug}: {error}")

    if not all_jobs:
        print("No jobs collected.")
        return

    combined_jobs = all_jobs[0]

    for jobs in all_jobs[1:]:
        combined_jobs = combined_jobs._append(
            jobs,
            ignore_index=True,
        )

    combined_jobs["job_id"] = range(1, len(combined_jobs) + 1)

    output_path = "data/01_raw/scraped_jobs.csv"
    combined_jobs.to_csv(output_path, index=False)

    print(f"Saved {len(combined_jobs)} jobs to {output_path}")


if __name__ == "__main__":
    main()