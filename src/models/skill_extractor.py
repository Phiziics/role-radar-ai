import re


class SkillExtractor:
    def __init__(self):
        self.skills = [
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "nlp",
            "rag",
            "llm",
            "fastapi",
            "streamlit",
            "docker",
            "mlflow",
            "scikit-learn",
            "pandas",
            "numpy",
            "spark",
            "databricks",
            "aws",
            "azure",
            "gcp",
            "power bi",
            "tableau",
            "excel",
            "a/b testing",
            "causal inference",
            "forecasting",
            "time series",
            "classification",
            "regression",
            "recommendation systems",
            "embeddings",
            "vector search",
            "model governance",
            "risk management",
            "data storytelling",
            "experimentation",
            "product analytics",
            "dashboard",
            "fastapi",
            "hugging face",
            "transformers",
            "prompt engineering",
            "api",
        ]

    def extract(self, text: str) -> list[str]:
        text = str(text).lower()
        found_skills = []

        for skill in self.skills:
            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):
                found_skills.append(skill)

        return sorted(set(found_skills))
    