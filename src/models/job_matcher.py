import pandas as pd

from src.models.skill_extractor import SkillExtractor


class JobMatcher:
    def __init__(self):
        self.skill_extractor = SkillExtractor()

    def score_jobs(self, resume_text: str, jobs: pd.DataFrame) -> pd.DataFrame:
        resume_skills = set(self.skill_extractor.extract(resume_text))

        scored_jobs = []

        for _, row in jobs.iterrows():
            job_description = str(row["description"])
            job_skills = set(self.skill_extractor.extract(job_description))

            matched_skills = resume_skills.intersection(job_skills)
            missing_skills = job_skills.difference(resume_skills)

            if len(job_skills) == 0:
                match_score = 0
            else:
                match_score = len(matched_skills) / len(job_skills)

            scored_jobs.append(
                {
                    "job_id": row.get("job_id"),
                    "company": row.get("company"),
                    "title": row.get("title"),
                    "location": row.get("location"),
                    "remote_type": row.get("remote_type"),
                    "job_url": row.get("job_url"),
                    "match_score": round(match_score, 3),
                    "matched_skills": ", ".join(sorted(matched_skills)),
                    "missing_skills": ", ".join(sorted(missing_skills)),
                    "required_skills": ", ".join(sorted(job_skills)),
                }
            )

        return pd.DataFrame(scored_jobs).sort_values(
            by="match_score",
            ascending=False,
        )