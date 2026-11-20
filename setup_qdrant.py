from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(
    host="localhost",
    port=6333
)

client.create_collection(
    collection_name="course_materials",
    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE
    )
)

print("Collection created!")
0

