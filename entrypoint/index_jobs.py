import pandas as pd

from src.rag.rag_engine import RAGEngine


def main():
    job_path = "data/01_raw/scraped_jobs.csv"

    jobs = pd.read_csv(job_path)
    jobs["description"] = jobs["description"].fillna("")
    jobs["title"] = jobs["title"].fillna("Unknown Title")
    jobs["company"] = jobs["company"].fillna("Unknown Company")
    jobs["location"] = jobs["location"].fillna("Unknown")
    jobs["remote_type"] = jobs["remote_type"].fillna("Unknown")
    jobs["job_url"] = jobs["job_url"].fillna("")

    documents = []

    for _, row in jobs.iterrows():
        document = f"""
        Company: {row["company"]}
        Title: {row["title"]}
        Location: {row["location"]}
        Remote Type: {row["remote_type"]}
        Job Description: {row["description"]}
        """
        documents.append(document)

    metadatas = jobs[
        [
            "company",
            "title",
            "location",
            "remote_type",
            "job_url",
        ]
    ].to_dict(orient="records")

    ids = jobs["job_id"].astype(str).tolist()

    rag = RAGEngine()
    rag.add_documents(
        documents=documents,
        metadatas=metadatas,
        ids=ids,
    )

    print(f"Indexed {len(documents)} jobs into ChromaDB.")


if __name__ == "__main__":
    main()