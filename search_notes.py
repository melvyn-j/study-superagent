from qdrant_client import QdrantClient
from ollama import embed

client = QdrantClient(
    host="localhost",
    port=6333
)

query = input("Question: ")

query_vector = embed(
    model="nomic-embed-text",
    input=query
)["embeddings"][0]

results = client.query_points(
    collection_name="course_materials",
    query=query_vector,
    limit=3
)

for i, point in enumerate(results.points, start=1):
    print(f"\n--- Result {i} ---")
    print(point.payload["source"])
    print()
    print(point.payload["text"][:500])
0

