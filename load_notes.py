from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from ollama import embed

client = QdrantClient(
    host="localhost",
    port=6333
)

text = (
    "The chain rule is used when differentiating "
    "composite functions."
)

embedding = embed(
    model="nomic-embed-text",
    input=text
)["embeddings"][0]

client.upsert(
    collection_name="course_materials",
    points=[
        PointStruct(
            id=1,
            vector=embedding,
            payload={"text": text}
        )
    ]
)

print("Stored successfully")
0

