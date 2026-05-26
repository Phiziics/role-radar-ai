from src.models.job_matcher import JobMatcher
from src.pipelines.ingestion_pipeline import JobIngestionPipeline


def main():
    ingestion = JobIngestionPipeline(
        job_path="data/01_raw/scraped_jobs.csv",
    )

    jobs = ingestion.load_jobs()
    resume_text = ingestion.load_resume("data/01_raw/resume.txt")

    matcher = JobMatcher()
    scored_jobs = matcher.score_jobs(
        resume_text=resume_text,
        jobs=jobs,
    )

    print(scored_jobs.head(20))

    scored_jobs.to_csv(
        "data/04_predictions/scored_jobs.csv",
        index=False,
    )

    print("Saved scored jobs to data/04_predictions/scored_jobs.csv")


if __name__ == "__main__":
    main()