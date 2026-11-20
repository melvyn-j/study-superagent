from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from ollama import embed

from services.pdf_loader import extract_text
from services.chunker import chunk_text


client = QdrantClient(
    host="localhost",
    port=6333
)


def ingest_pdf(pdf_path):

    text = extract_text(pdf_path)

    chunks = chunk_text(text)

    points = []

    for idx, chunk in enumerate(chunks):

        vector = embed(
            model="nomic-embed-text",
            input=chunk
        )["embeddings"][0]

        points.append(
            PointStruct(
                id=idx + 100,
                vector=vector,
                payload={
                    "text": chunk,
                    "source": pdf_path
                }
            )
        )

    client.upsert(
        collection_name="course_materials",
        points=points
    )

    print(
        f"Loaded {len(points)} chunks."
    )
0

0

