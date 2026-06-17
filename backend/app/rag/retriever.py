from sentence_transformers import SentenceTransformer
import faiss
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("knowledge.index")

documents = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
folder = os.path.join(BASE_DIR, "knowledge")

for file in os.listdir(folder):

    with open(os.path.join(folder, file), "r") as f:
        documents.append(f.read())


def retrieve(query):

    embedding = model.encode([query])

    distances, indices = index.search(embedding, 3)

    results = []

    for i in indices[0]:
        results.append(documents[i])

    return results