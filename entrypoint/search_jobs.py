from src.rag.rag_engine import RAGEngine


def main():
    rag = RAGEngine()

    query = input("Ask the job market: ")

    results = rag.retrieve(
        query=query,
        top_k=5,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for i, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances),
        start=1,
    ):
        print("=" * 80)
        print(f"Result {i}")
        print(f"Company: {metadata.get('company')}")
        print(f"Title: {metadata.get('title')}")
        print(f"Location: {metadata.get('location')}")
        print(f"Remote Type: {metadata.get('remote_type')}")
        print(f"Job URL: {metadata.get('job_url')}")
        print(f"Distance: {round(distance, 4)}")
        print("-" * 80)
        print(document[:1500])


if __name__ == "__main__":
    main()