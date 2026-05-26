import pandas as pd


class JobIngestionPipeline:
    def __init__(self, job_path: str):
        self.job_path = job_path

    def load_jobs(self) -> pd.DataFrame:
        jobs = pd.read_csv(self.job_path)
        jobs["description"] = jobs["description"].fillna("")
        return jobs

    def load_resume(self, resume_path: str) -> str:
        with open(resume_path, "r", encoding="utf-8") as file:
            return file.read()