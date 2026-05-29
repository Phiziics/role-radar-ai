import chromadb
from sentence_transformers import SentenceTransformer


class RAGEngine:
    def __init__(
        self,
        collection_name: str = "role_radar_jobs",
        db_path: str = "data/03_features/chroma_db",
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        self.model = SentenceTransformer(model_name)
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
        )

    def add_documents(
        self,
        documents: list[str],
        metadatas: list[dict],
        ids: list[str],
    ) -> None:
        embeddings = self.model.encode(documents).tolist()

        self.collection.upsert(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

    def retrieve(self, query: str, top_k: int = 5) -> dict:
        query_embedding = self.model.encode([query]).tolist()[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return results