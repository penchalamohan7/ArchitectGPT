from sentence_transformers import SentenceTransformer
import faiss
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

folder = os.path.join(BASE_DIR, "knowledge")

for file in os.listdir(folder):

    with open(os.path.join(folder, file), "r") as f:
        texts.append(f.read())

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(384)

index.add(embeddings)

faiss.write_index(index, "knowledge.index")